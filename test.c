int calculateMatrixSum(int rows, int columns, int **matrix)
{  
    int i, j, sum=0;
    if((rows>0)&&(columns>0))
    {
        for(i=0;i<rows;i++)
        { 
            sum =0;
            for(j=0;j<columns;j++)
            {
                if(i==j)
                { 
                    if(matrix[i][j]/2!=0)
                        sum += matrix[i][i];
                }
            } 
        } 
        return sum;
    }
    else
        return sum;    
}