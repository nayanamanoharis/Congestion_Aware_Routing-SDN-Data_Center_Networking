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

void * sockprog(void *filename){
	int rqst = 0;
	int i,a;
	int j,k;
	int tcpfd;
	int nbytes;
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
    
    
	FILE *fp;
	char *file_name=(char *)filename;
    
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
            
			struct addrinfo hints, *servinfo, *p;
			int rv;
			memset(&hints, 0, sizeof hints); 
			hints.ai_family = AF_INET;
			hints.ai_socktype = SOCK_STREAM;
			if ((rv = getaddrinfo(ip, token3, &hints, &servinfo)) != 0) {
				fprintf(stderr, "getaddrinfo: %s\n", gai_strerror(rv));
				return 0;
			}
			for(p = servinfo; p != NULL; p = p->ai_next){
				if ((tcpfd = socket(AF_INET, SOCK_STREAM, 0)) < 0) 
				{
                    
					perror("cannot create socket\n");
					continue;
				}    
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
                printf("value =%d\n",val);
				if(val>max_send_size){
					if((send_bytes = send(tcpfd,name3,max_send_size, 0)) == -1)
				    perror("send error1");
                    
                   printf("No of bytes sent %d\n",send_bytes);
					val-=max_send_size;
				}
				else{
					if( (send(tcpfd,name3,val, 0)) == -1)
						perror("send error2");
					val=0;
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
	pthread_create(&sockprogram, NULL,sockprog,(void *)argv[1]);
	pthread_join(sockprogram,NULL);
	return 0;
}
