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
#include <ifaddrs.h>


 
int MAXMSG=1500;

int count=0;

/* referred from the links on Piazza Byte stream socket example */

int
read_from_client (int file)
{
    char name[MAXMSG];
    int nbytes;
    int totalsize=0;

    nbytes = read(file, name, MAXMSG);

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
    struct ifaddrs *ifap, *ifa;
    struct sockaddr_in *sa;
    char *addr;
    char *addr1;
    int sockoptval=1;
     

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
        
    /*  TCP socket creating beejs tutorials */    
        
    struct sockaddr_in socket_temp;
    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0)
        perror("cannot create socket");
        
        /* stack overflow*/
        
        getifaddrs (&ifap);
    for (ifa = ifap; ifa; ifa = ifa->ifa_next) {
        if (ifa->ifa_addr->sa_family==AF_INET) {
            sa = (struct sockaddr_in *) ifa->ifa_addr;
            if(strstr(ifa->ifa_name ,"eth0")!=0)
            {
                addr1 = inet_ntoa(sa->sin_addr);
                printf("Address:= %s",addr1);
                
            }
            //   addr = inet_ntoa(sa->sin_addr);
            //printf("Interface: %s\tAddress: %s\n", ifa->ifa_name, addr1);
        }
    }    
        
        
    socket_temp.sin_family = AF_INET;
    socket_temp.sin_port = htons (atoi(line));
    socket_temp.sin_addr.s_addr =inet_addr(addr1);
        
      setsockopt(sock, SOL_SOCKET, SO_REUSEADDR, &sockoptval, sizeof(int));    
    
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
        freeifaddrs(ifap);
        
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

