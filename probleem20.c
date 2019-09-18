#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

double**cross_pdt(double**a,double**b);
double** line_dir_pt(double** m,double** A,double k1,double k2);
double**meshgrid(int len, int start, int stepX, int stepY);
void findingZ(double**n,double c,double**x,double**y,double**z,int len);
double det(double** m);
double** createVec(double x,double y,double z);
double **vstack(double** n1,double** n2, double** n3);
 
int  main() //main function begins
{
int len = 2;
double k=0;

// Normal vectors of planes
double **n1 = createVec(1, k,-1);
double **n2 = createVec(k,-1,-1);
double **n3 = createVec(1, 1,-k);

savetxt(n1,"n1.dat",3,1);
savetxt(n2,"n2.dat",3,1);
savetxt(n3,"n3.dat",3,1);

// Direction vector of line
double **l=cross_pdt(n1,n2);
savetxt(l,"l.dat",3,1);

// Point on line
double **O = createMat( 3, 1);
savetxt(O,"O.dat",3,1);

double **T =line_dir_pt(l,O,-20,20);
savetxt(T,"T.dat",3,10);

// Creating planes
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
findingZ(n3,c3,x2,y2,z2,len);

savetxt(x,"x.dat",len,len);
savetxt(y,"y.dat",len,len);
savetxt(z,"z.dat",len,len);
savetxt(x2,"x2.dat",len,len);
savetxt(y2,"y2.dat",len,len);
savetxt(z1,"z1.dat",len,len);
savetxt(z2,"z2.dat",len,len);

// Verification
k = 0;
n1 = createVec(1, k,-1);
n2 = createVec(k,-1,-1);
n3 = createVec(1, 1,-k);
double **case1 = vstack(n1,n2,n3);
printf("Case 1 : k = 0\n"); print(case1,3,3);
printf("Det = %lf\n\n",det(case1));

k = 1;
n1 = createVec(1, k,-1);
n2 = createVec(k,-1,-1);
n3 = createVec(1, 1,-k);
double **case2 = vstack(n1,n2,n3);
printf("Case 2 : k = 1\n"); print(case2,3,3);
printf("Det = %lf\n\n",det(case2));

k = -1;
n1 = createVec(1, k,-1);
n2 = createVec(k,-1,-1);
n3 = createVec(1, 1,-k);
double **case3 = vstack(n1,n2,n3);
printf("Case 3 : k = -1\n"); print(case3,3,3);
printf("Det = %lf\n\n",det(case3));

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
double det(double** m){
	return (m[0][0]*((m[1][1]*m[2][2])-(m[1][2]*m[2][1])))-(m[0][1]*((m[1][0]*m[2][2])-(m[1][2]*m[2][0])))+(m[0][2]*((m[1][0]*m[2][1])-(m[1][1]*m[2][0])));
}
double** createVec(double x,double y,double z){
	double** vec = createMat(3,1);
	*vec[0]=x; *vec[1]=y; *vec[2]=z;
	return vec;
}
double **vstack(double** n1,double** n2, double** n3){
	double **nn = createMat(3,3);
	nn[0][0] = *n1[0]; nn[0][1] = *n1[1]; nn[0][2] = *n1[2];
	nn[1][0] = *n2[0]; nn[1][1] = *n2[1]; nn[1][2] = *n2[2];
	nn[2][0] = *n3[0]; nn[2][1] = *n3[1]; nn[2][2] = *n3[2];
	return nn;
}
