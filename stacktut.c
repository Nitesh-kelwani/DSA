#include<stdio.h>
#include<stdlib.h>

struct stack
{
    int size;
    int top;
    int *arr;
};

int isempty(struct stack*ptr){
    if (ptr->top==-1)
    {
        return 1;
    }
    else
    { 
    return 0;
    }
    
}
int isfull(struct stack*ptr){
    if (ptr->top==ptr->size-1)
    {
        return 1;
    }
  
  else 
     {  return 0;
  }
    
}
void push(struct stack*ptr,int val){
    if (isfull(ptr))
    {
        printf("Stack overflow");
    }
    else{
        ptr->top++;
        ptr->arr[ptr->top]=val;
    }
    
}
 int pop(struct stack*ptr){
        if (isempty(ptr))
        {
            printf("Stack underflow");
            return -1;;
        }
        else{
            int val=ptr->arr[ptr->top];
            ptr->top--;
            return val;
        }
        
 }
int main(){
    struct stack *s = (struct stack *) malloc(sizeof(struct stack));
    s->size=50;
    s->top=-1;
    s->arr=(int *) malloc(s->size*sizeof(int));
   
    push(s,22);
    push(s,56);
    push(s,85 );
   printf("%d",isfull(s));
   printf("%d",isempty(s));
    return 0;
}