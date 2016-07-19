#include <stdio.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <string.h>
#include <netdb.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <errno.h>
#include <arpa/inet.h>
#include <sys/wait.h>

 
int MAXMSG=1500;

int count=0;


int
read_from_client (int file)
{
    char name[MAXMSG];
    int nbytes;
    int totalsize=0;

    nbytes = read(file, name, MAXMSG);
   // printf("Read bytes: %d\n",nbytes);
    totalsize+=nbytes;
    count++;
    if (nbytes < 0)
    {
        perror ("read");
        exit (EXIT_FAILURE);
    }

    else if (nbytes == 0)
        return -1;
    else
    {
        fprintf (stderr, "Server: got message: `%s'\n", name);
        return 0;
    }
}

    

int main(int argc, char *argv[])
{
    FILE *fd; 
    char line[10];
    int i;
    int j=0,k=0;
    int max=0;
    int socketsvc[20];
    int new;
    fd_set active_fd_set, read_fd_set;
    struct sockaddr_in clientname;
    socklen_t size;
    int sock=0;
    
     

    fd = fopen(argv[1],"r");
    if(fd == NULL)
    {
        perror("Error opening the file");
        return(-1);
    } 
    FD_ZERO (&active_fd_set); 
    FD_ZERO (&read_fd_set); 

    while(fgets (line, sizeof line, fd) != NULL) 
    {
       // sock_desp_list[j]=create_socket(atoi(line));
        
    struct sockaddr_in socket_temp;
    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0)
        perror("cannot create socket");
        
    socket_temp.sin_family = AF_INET;
    socket_temp.sin_port = htons (atoi(line));
    socket_temp.sin_addr.s_addr = htonl (INADDR_ANY);
    
    if (bind(sock, (const struct sockaddr *)&socket_temp, sizeof(socket_temp)) < 0)
        perror("bind failed\n");
    printf("Bind Successful\n");   
        socketsvc[j]=sock;
    
        if (listen(socketsvc[j], 5) < 0) 
        {
            perror("listen failed\n");
            exit(1);
        }
        printf("Listen Successful: %d, %d\n", socketsvc[j], j);
        FD_SET (socketsvc[j], &active_fd_set);
        j++;
    }

    fclose(fd);
    k=j;
   

    while (1)
    {
        int value=0;
        read_fd_set = active_fd_set;
        if (select (FD_SETSIZE, &read_fd_set, NULL, NULL, NULL) < 0)
        {
            perror ("select");
            exit (EXIT_FAILURE);
        }
      //  printf("Select Successful\n");

        for (i = 0; i < FD_SETSIZE; ++i)
        {    
            if (FD_ISSET(i, &read_fd_set))
            { 
                unsigned j;
                
                  for(j=0;j < k;j++)
                  {

                    if (i == socketsvc[j])
                    {
                        value=1;
                        size = sizeof (clientname);
                        new = accept (i, (struct sockaddr *) &clientname,
                                &size);
    
                        if (new < 0)
                        {
                            perror ("accept");
                            exit (EXIT_FAILURE);
                        }
                        fprintf (stderr,
                                "Server: connect from host %s, port %hd.\n",
                                inet_ntoa (clientname.sin_addr),
                                ntohs (clientname.sin_port)); 
                        FD_SET(new, &active_fd_set);
                    }
                  FD_CLR(socketsvc[j],&read_fd_set);
                  }
                    if(value==0)
                    {
                        if (read_from_client (i) < 0)
                        {  
                            close (i);
                            FD_CLR (i, &active_fd_set);
                        }
                   }
            }      
        }
    }
}
