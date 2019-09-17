#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

double**cross_pdt(double**a,double**b);
double** line_dir_pt(double** m,double** A,double k1,double k2);
double**meshgrid(int len, int start, int stepX, int stepY);
void findingZ(double**n,double c,double**x,double**y,double**z,int len);
 
int  main() //main function begins
{
int len = 2;
double k=1;
//vectors parallel to given lines
double **n1 = createMat( 3, 1);
n1[0][0]=1; n1[1][0]=k; n1[2][0]=-1;
savetxt(n1,"n1.dat",3,1);

double **n2 = createMat( 3, 1);
n2[0][0]=k; n2[1][0]=-1; n2[2][0]=-1;
savetxt(n2,"n2.dat",3,1);

double **n3 = createMat( 3, 1);
n3[0][0]=1; n3[1][0]=1; n3[2][0]=-k;
savetxt(n3,"n3.dat",3,1);
//points on line
double **l=cross_pdt(n1,n2);
savetxt(l,"l.dat",3,1);

double **O = createMat( 3, 1);
savetxt(O,"O.dat",3,1);

double **T =line_dir_pt(l,O,-20,20);
savetxt(T,"T.dat",3,10);

double**x = meshgrid(len, -20, 40, 0);
double**y = meshgrid(len, -20, 0, 40);
double**z = meshgrid(len, -20, 0, 0);
double**z1 = meshgrid(len, -20, 0, 0);

double**x2 = meshgrid(len, -20, 40, 0);
double**y2 = meshgrid(len, -20, 0, 40);
double**z2 = meshgrid(len, -20, 0, 0);

double c1=0,c2=0,c3=0;
findingZ(n1,c1,x,y,z,len);
findingZ(n2,c2,x,y,z1,len);
//*n3[1] += *n3[2]; *n3[2] = *n3[1] - *n3[2]; *n3[1] -= *n3[2];
findingZ(n3,c3,x2,y2,z2,len);
savetxt(x,"x.dat",len,len);
savetxt(y,"y.dat",len,len);
savetxt(z,"z.dat",len,len);
savetxt(x2,"x2.dat",len,len);
savetxt(y2,"y2.dat",len,len);
savetxt(z1,"z1.dat",len,len);
savetxt(z2,"z2.dat",len,len);
return 0;
}
double**cross_pdt(double**a,double**b)
{
double**n = createMat(3,3);
n[0][0]=0; n[0][1]=-*a[2]; n[0][2]=*a[1];
n[1][0]=*a[2]; n[1][1]=0; n[1][2]=-*a[0];
n[2][0]=-*a[1]; n[2][1]=*a[0]; n[2][2]=0;
return matmul(n,b,3,3,1);
}
double**meshgrid(int len, int start, int stepX, int stepY){
double ** ret = createMat(len, len);
for (int i=0; i<len; i++)
for (int j=0; j<len; j++){
ret[i][j] = start + i*stepY + j*stepX;
}
return ret;
}
double** line_dir_pt(double** m,double** A,double k1,double k2)
{
int len = 10;
double** x_AB = createMat(3,len);
double** lam = linspace(k1,k2,len);
for(int i=0; i<len; i++){
x_AB[0][i] = *A[0] + *lam[i]*(*m[0]);
x_AB[1][i] = *A[1] + *lam[i]*(*m[1]);
x_AB[2][i] = *A[2] + *lam[i]*(*m[2]);
}
return x_AB;
}
void findingZ(double**n,double c,double**x,double**y,double**z,int len)
{
	
for (int i=0; i<len; i++)
	for (int j=0; j<len; j++)
		z[i][j] = ((c-*n[0]*x[i][j]-*n[1]*y[i][j])*1.0) / (*n[2]); 
}
