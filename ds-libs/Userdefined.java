import java.util.*;
public class Userdefined
{
    
     static void BubbleSort(int num[])  //Sorting
    {
        int len=num.length;
        int i,j, temp;
        for(i=0;i<len;i++)
        {
            for( j=0;j<len-i-1;j++)
            {
                if(num[j]>num[j+1])
                {
                    temp=num[j];
                    num[j]=num[j+1];
                    num[j+1]=temp;
                   
                }
            }
        }
   //   System.out.println("Sorted Elements:");
        for(int k=0;k<len;k++)
         System.out.print(num[k]+"\t");
          System.out.println(); 
    }
     static void BinSearch(int num[],int k)  //Binary Search
     {
         int l=0,u=num.length-1;
         int m=0, found=0;
         while(l<=u)
         {
         m= (l+u)/2;
         if( k > num[m])
            l =m+1;
            else if( k< num[m])
            u=m-1;
            else
            {
                found =1;
                break;
                
            }
       
        }
        if(found==1)
         System.out.println(" Element Present at"+" "+ (m+1) +" " +"after sorting");
        
         else
          System.out.println("Not Present");
        }
      public static void main(String [] args)
      {
          Scanner sc=new Scanner(System.in);
          System.out.println( "Enter the total number of elements in the array:");
          int n=sc.nextInt();
          int a[]=new int[n];
          System.out.println( "Enter the elements:");
          for(int i=0;i<n;i++)
          {
          a[i]=sc.nextInt();
          }
         System.out.println("Entered Elements");
          for(int i=0;i<n;i++)
          {
          
       System.out.print(a[i]+"\t");

           }
     System.out.println();
      System.out.println("Elements should be sorted before Binary Search .....\n                                                                                                                                         ..Sorted Elements....");
       BubbleSort(a);                         //invoking BubbleSort ()
      
       System.out.println("Binary Search \n");
       
       System.out.println("Enter element to search");
       int ky=sc.nextInt();
       BinSearch(a, ky); // invoking Binary search method 
    }
     
}
