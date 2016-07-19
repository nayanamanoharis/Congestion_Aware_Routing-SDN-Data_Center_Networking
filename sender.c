#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <netdb.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <sys/wait.h>
#include <stdbool.h>
#include <pthread.h>
#include <ifaddrs.h>

char dip[30]={0};        
char Psize[1000]={0};
int Destination_PORT=0;
int number_value =0;
//pthread_mutex_t mx=PTHREAD_MUTEX_INITIALIZER; 



void *get_flow_state(void *pointer)
{    
int PORT1 = 5000;    
int rqst1 = 0; 
int optval = 1;
struct sockaddr_in servaddr3; 
socklen_t alen = sizeof(servaddr3);
int svc;
int nbytes;                        
char name2[1024]={0};
char name4[1024]={0};
int i;
struct ifaddrs *ifap, *ifa;
struct sockaddr_in *sa;
char *addr;
char *addr1; 
int sockoptval = 1;
char hostname[128];    
gethostname(hostname, 128);
char send_size[1000]={0};
char dip_address[30]={0};
int D_PORT=0; 
int cou=0;
int count=0; 
int number =0;
char left_value[50]={0};
char total_flow_size[30]={0};
char name5[50]={0};
char name6[30]={0};    
    
    
/* TCP SOCKETS CREATION referred from beejs guide and Rutgers guide */ 
	if ((svc = socket(AF_INET, SOCK_STREAM, 0)) < 0) 
    {
		perror("cannot create socket\n");
        exit(1);
		
	}
    //Aprintf("flow socket created = %d\n",svc);
    

    setsockopt(svc, SOL_SOCKET, SO_REUSEPORT, &optval, sizeof(optval));
       
    
    
    setsockopt(svc, SOL_SOCKET, SO_REUSEADDR, &sockoptval, sizeof(int));
    
    
    /* Referred from stack overflow  */
    
    getifaddrs (&ifap);
    for (ifa = ifap; ifa; ifa = ifa->ifa_next) {
        if (ifa->ifa_addr->sa_family==AF_INET) {
            sa = (struct sockaddr_in *) ifa->ifa_addr;
          //  addr = inet_ntoa(sa->sin_addr);
           // printf("Interface: %s\tAddress: %s\n", ifa->ifa_name, addr);
            if(strstr(ifa->ifa_name ,"eth1")!=0)
            {
                addr1 = inet_ntoa(sa->sin_addr);
                
            }
            //   addr = inet_ntoa(sa->sin_addr);
        //    printf("Interface: %s\tAddress: %s\n", ifa->ifa_name, addr);
        }
    }    
    freeifaddrs(ifap);
    //Aprintf("my address = %s\n",addr1);
        
	memset((char*)&servaddr3, 0, sizeof(servaddr3));  
	servaddr3.sin_family = AF_INET;
    servaddr3.sin_addr.s_addr = inet_addr(addr1); 
	servaddr3.sin_port = htons(PORT1);
    
    
	if (bind(svc, (struct sockaddr *)&servaddr3, sizeof(servaddr3)) < 0)
    {
        //Aprintf(" Bind failed error flow state");
		perror("bind failed");
        exit(1);
		
	}
    
    //Aprintf("Bind successfull for %d\n",svc);

	if (listen(svc, 5) < 0) 
    {
		perror("listen failed");
        exit(1);
		
	}
    
       
      
  //Aprintf("listen sucessfull for %d\n",svc);
    
    while(1)
        {
        
      fprintf(stderr,"\n \n \n The Server 3 has TCP port number 5000 ");
		while ((rqst1 = accept(svc, (struct sockaddr *)&servaddr3, &alen)) < 0) 
        {          
            if((errno!= ECHILD) && (errno!= ERESTART) && (errno != EINTR))
            {
                perror("accept failed"); 
                exit(1);
            }
         }
        
        
        //pthread_mutex_lock(&mx);  
        for(cou=0; cou<1000;cou++)
        {
          send_size[cou]=Psize[cou];  
        }
        for(cou=0;cou<30;cou++)
        {
            dip_address[cou]= dip[cou];
        }
        D_PORT = Destination_PORT; 
        //pthread_mutex_unlock(&mx);
        
        for(count=0;count<30;count++)
        {
           name4[count]= dip_address[count];
        }
               
        //pthread_mutex_lock(&mx);
        number = number_value; 
        //pthread_mutex_unlock(&mx);
        
        snprintf(left_value, 50, "%d", number);
        //Aprintf("\n left_value: %s\n",left_value);
        
        for(count=0; count<50;count++)
        {
          name4[count+32]=left_value[count];    
        }
        
        for(count=0;count<30;count++)
        {
            name4[count+54] = send_size[count];
        }
        puts(name2);
        
                   
      nbytes = read(rqst1, name2, 1500); 

    //Aprintf("Reading socket num %d and data read %s\n",rqst1,name2);
        
 // inet_ntop(AF_INET,&(servaddr2.sin_addr),ip4,INET_ADDRSTRLEN); 
        
fprintf(stderr,"\n \n Server 3 received a request with key %s from Server 2 with port number %d and IP address",name2,PORT1);
        
   
        nbytes = write(rqst1, name4, 100); 

    fprintf(stderr,"\n \n The Server 3 sends the reply %s to Server 2 with port number %d and IP address",name4,PORT1);
      
      memset(send_size,0,1000);
      number = 0;
      memset(left_value,0,50);
      memset(name4,0,1024);    
                
                   
    close(rqst1);    
        
  }       
    
}


void * command_parser(void *filename)
{
	int rqst = 0;
	int a,b;
	int j,k;
	int tcpfd;
	char name3[1500]={};
	long int size = 0;
	int val;
	int PORT=0;
	int thousand=0,unit=0,mega=0;
	const char s[2] = " ";
	char *token;
	char *token1;
	char *token2;
	char *token3;
	char *token4;
	char *token5;
	char line[100];
	char value[1000];
	char ip[30]={0};
    int send_bytes =0;
    int gou=0;
    int gount=0;
    char size_value[1000]={0};
    int size_value_int =0;
    
	FILE *fp;
	char *file_name=(char *)filename;
    //Aprintf("file name =%s",file_name);
    
	fp=fopen(file_name, "r");
	if(fp == NULL) 
	{
		perror("Error opening file");
		return 0;
	}
	if(fp != NULL)
	{
		while(fgets(line, 100, fp))
		{
			token = strtok(line, s);
			token1 = strtok(NULL,s);
			token2 = strtok(NULL,s);
			token3 = strtok(NULL,s); 
			token4 = strtok(NULL,s);
			token5 = strtok(NULL,s);
			PORT = atoi(token3);
			strcpy(ip,token1);     
			strcpy(value,token5);
            
            //pthread_mutex_lock(&mx); 
            Destination_PORT = PORT;
            for(gou=0;gou<30;gou++)
            {
                dip[gou]=ip[gou];
            }
            //pthread_mutex_unlock(&mx);
            
			size = 0;
			thousand = 0;
			mega = 0;
            
			for(a=0;a<strlen(value);a++)
			{
				if(value[a]== 'K' || value[a] == 'k')
				{   
					value[a] = '\0';
					thousand++;
				}
				else if(value[a] == 'M' || value[a] == 'm')
				{   
					value[a] = '\0';
					mega++;
				}
			}
			if(thousand)
				size = 1000*(atol(value));
			else if(mega)
				size = 1000*1000*(atol(value));
			else 
				size = (atol(value));
 
			thousand = 0;
			mega = 0;    
            
            size_value_int = size;
            
            sprintf(size_value,"%d",size_value_int);
            
            //pthread_mutex_lock(&mx);
            
            memset(Psize,0,1000);
            
            for(gou=0;gou<1000;gou++)
            {
                Psize[gou]=size_value[gou];
            }
            
            memset(size_value,0,1000);
            
            //pthread_mutex_unlock(&mx);
            
            
            
        /* Beejs guide */            
			struct addrinfo hints, *servinfo, *p;
			int rv;
			memset(&hints, 0, sizeof hints); 
			hints.ai_family = AF_INET;
			hints.ai_socktype = SOCK_STREAM;
			if ((rv = getaddrinfo(ip, token3, &hints, &servinfo)) != 0) {
				fprintf(stderr, "getaddrinfo: %s\n", gai_strerror(rv));
				return 0;
			}
           
            //Aprintf("ip and port it is connecting to %s %s",ip,token3);
            
			for(p = servinfo; p != NULL; p = p->ai_next){
				if ((tcpfd = socket(AF_INET, SOCK_STREAM, 0)) < 0) 
				{
                    
					perror("cannot create socket\n");
					continue;
				}
                
                //Aprintf("Socket created %d\n",tcpfd);
				if (connect(tcpfd, p->ai_addr, p->ai_addrlen) < 0)
				{
					close(tcpfd);
					perror("connect failed\n");
					continue;
				}
				break;
			}
			freeaddrinfo(servinfo);
			val=size;
			int max_send_size=1500;			
			while(val)
			{
                //Aprintf("value =%d\n",val);
				if(val>max_send_size){
					if((send_bytes = send(tcpfd,name3,max_send_size, 0)) == -1)
				    perror("send error1");
                    
                   //Aprintf("No of bytes sent %d\n",send_bytes);
					val-=max_send_size;
                    
                   // pthread_mutex_lock(&mx);
                    number_value = val;
                   // pthread_mutex_unlock(&mx);
                    
				}
				else{
					if( (send(tcpfd,name3,val, 0)) == -1)
						perror("send error2");
					val=0;
                    
                   // pthread_mutex_lock(&mx);
                    number_value = val;
                   // pthread_mutex_unlock(&mx);
				}
			}
			close(tcpfd);  
		}
	}
	else 
	{
		fscanf(fp, "%s", line);
	}
	fclose(fp);
}


int main(int argc, char **argv)
{
	pthread_t sockprogram,controllerprog;
	pthread_create(&sockprogram, NULL,command_parser,(void *)argv[1]);
    pthread_create(&controllerprog, NULL, get_flow_state,NULL);     
	pthread_join(sockprogram,NULL);
    pthread_join(controllerprog,NULL);
	return 0;
}