#include <stdio.h>
#include <stdlib.h>

/*
 * SINGLE LINKED LIST
 * ------------------
 *
 *  HEAD --> NODE_0 --> NODE_1 --> NODE_2 --> NODE_3 --> NODE_4 --> NULL
 *            
 */

#define TRUE  0
#define FALSE 1

/* User defined structure */
typedef struct _node_t
{
    int              data;
    struct _node_t  *next;
} node_t, *ptr_node_t;

/* User defined data types */
typedef  unsigned  int   uint32_t;
typedef  unsigned  char  uint8_t;

ptr_node_t sll_print( ptr_node_t head )
{
    ptr_node_t cur = head;
    while( cur )
    {
        printf("%d --> ", cur->data);
        cur = cur->next;
    }
    printf("NULL\n\n");
    return head;
}

ptr_node_t sll_reverse( ptr_node_t head )
{
    ptr_node_t  new  = NULL;
    ptr_node_t  cur  = head;
    ptr_node_t  prev = NULL;

    while( cur )
    {
        new = cur->next;
        cur->next = prev;
        prev = cur;
        cur = new;
    }

    return (head = prev);
}

ptr_node_t sll_add_element_to_end( ptr_node_t head )
{
    ptr_node_t new = NULL;
    ptr_node_t cur = NULL;
    uint8_t     ch = '\0';
    uint32_t  data = 0;

    if( head == NULL )
    {
        printf("Press 'Y' to add a new element to SLL\n");
        scanf(" %c", &ch);
        if( ch != 'Y' )
          return head;

        head = (ptr_node_t) calloc( sizeof( node_t ), 1 );
        if( head )
        {
            printf("Enter the data to add to linked list at the start\n");
            scanf("%d", &data);

            head->next = NULL;
            head->data = data;
        }
        else
        {
            printf("Memory Allocation failure\n");
            return head;
        }
    }

    while( 1 )
    {
        printf("Press 'Y' to add a new element to SLL\n");
        scanf(" %c", &ch);
        if( ch == 'Y' )
        {
            new = (ptr_node_t) calloc( sizeof(node_t), 1 );
            if( new )
            {
                printf("Enter the data to add to linked list at the end\n");
                scanf("%d", &data);

                cur = head;
                while( cur->next )
                    cur = cur->next;

                cur->next = new;
                new->data = data;
                new->next = NULL;
            }
            else
            {
                printf("Memory Allocation failure\n");
                return head;
            }
        }
        else
        {
            return head;
        }
    }
}

ptr_node_t sll_add_element_to_start( ptr_node_t head )
{
    uint32_t data = 0;
    uint8_t  ch   = '\0';
    
    if( head == NULL )
    {
        printf("Press 'Y' to add a new element to SLL\n");
        scanf(" %c", &ch);
        if( ch != 'Y' )
          return head;

        head = (ptr_node_t) calloc( sizeof( node_t ), 1 );
        if( head )
        {
            printf("Enter the data to add to linked list at the start\n");
            scanf("%d", &data);

            head->next = NULL;
            head->data = data;
        }
        else
        {
            printf("Memory Allocation failure\n");
            return head;
        }
    }

    do
    {
        ptr_node_t new;

        printf("Press 'Y' to add a new element to SLL\n");
        scanf(" %c", &ch);
        if( ch != 'Y' )
          return head;

        printf("Enter the data to add to linked list at the start\n");
        scanf("%d", &data);

        new = (ptr_node_t) calloc( sizeof( node_t ), 1 );
        if( new )
        {
            //new->next = head->next;
            //new->data = data;
            //head->next = new;
            new->next = head;
            new->data = data;
            head = new;
        }
        else
        {
            printf("Memory Allocation failure\n");
            return head;
        }

    } while( 1 );

    return head;
}

int main( void )
{
    /* Head Node/Element */
    ptr_node_t head = NULL;

    /* Add elements to end */
    head = sll_add_element_to_end( head );

    /* Add elements to end */
    //head = sll_add_element_to_start( head );
    if( head )
    {
        /* Print all elements of SLL */
        head = sll_print( head );
    }

    /* Add elements to end */
    head = sll_reverse( head );
    if( head )
    {
        /* Print all elements of SLL */
        head = sll_print( head );
    }

    return TRUE;
}

