% PUNTO 1
%Se define el vector de valores para el eje y (valores señal)
h = [ 0 1 0 1 0 1 0 1 0 1 ];
%Se define el vector de los valores para el eje x (tiempo)
x = [ 1 2 3 4 5 6 7 8 9 10 ];
%Se hace la gráfica con la función stairs relacionando el tiempo con los
%valores de la señal 
stairs(x,h)
%Se definen los valores de los ejes para que la grafica se muestre a una escala
%visualmente mejor
axis equal 
% PUNTO 2
%Se define el vector de valores para el eje y (valores señal)
h=[1 1 0 1 0 0 1 1 0 1];
 %Se define la variable incial para el ciclo while 
 n=1;
 %Se da al vector h un valor de 1 en la posición 11 para evitar un error en
 %uno de los if.
 h(11)=1;
 %Se inicia el ciclo while para n menor o igual a 10 para recorrer las
 %posiciones del vector h.
 while n<=10;
 %Se crea el vector t de n-1 hasta n con paso de 0.001
 t=n-1:0.001:n;
 %Se hace un condicional if al que se entra cuando el vector h en la
 %posición n toma el valor de 0
 if h(n) == 0
 %Se realiza un nuevo if dentro del anterior al que se entra si el valor
 %del vector h en la posicion n+1 es igual a 0
 if h(n+1)==0
 %Se asigna a y un valor de t mayor a n
 y=(t>n);
 %Se da la condicion contraria al anterior if
 else
 %Se asigna a y un valor de t igual a n
 y=(t==n);
 %Se finaliza el condicional if anterior
 end
 %Se realiza la asignacion a d dandole a graficar t con y, dandole titulo a
 %la grafica y activando la cuadricula de la misma.
 d=plot(t,y); title ('DDDDDDDDDD');grid on;
 %Se define en 2.5 el ancho de las lineas para la grafica d
 set(d,'LineWidth',2.5);
 %Se usa el comando hold on para mantener el estado de la grafica
 hold on;
 %Se definen los limites de los ejes de la grafica para x de 0 a 10 y para
 %y de -1.5 a 1.5
 axis([0 10 -1.5 1.5]);
 %Se da la condicion contraria al primer if
 else
 %Se crea un if dentro de la condicion contraria del primer if al que se
 %entra cuando el vector h en la posicion n+1 es igual a 0
 if h(n+1)==0
 %Se le asigna a y un valor de t menor a n y se le resta la multiplicacion de 0 por t igual a n
 y=(t<n)-0*(t==n);
 %Se inicia la condicion contraria del anterior if
 else
 %Se le asigna a y un valor de t menor a n y se le resta la multiplicacion de 1 por t igual a n
 y=(t<n)+1*(t==n);
 %Se termina el anterior if
 end
 %Se realiza la asignacion a d dandole a graficar t con y, dandole titulo a
 %la grafica y activando la cuadricula de la misma.
 d=plot(t,y);title('CCCCCCCCCC');grid on;
 %Se define en 2.5 el ancho de las lineas para la grafica d
 set(d,'LineWidth',2.5);
 %Se usa el comando hold on para mantener el estado de la grafica
 hold on;
 %Se definen los limites de los ejes de la grafica para x de 0 a 10 y para
 %y de -1.5 a 1.5
 axis([0 10 -1.5 1.5]);
 %Se finaliza el primer condicional if
 end
 %Se suma 1 al valor de n
 n=n+1;
 %Se finaliza el ciclo while
 end
% PUNTO 4
h=rand(1,11);
 n=1;
 h(11)=1;
 while n<=10;
 t=n-1:0.001:n;
 if h(n) == 0
 if h(n+1)==0
 y=(t>n);
 else
 y=(t==n);
 end
 d=plot(t,y); title ('DDDDDDDDDD');grid on;
 set(d,'LineWidth',2.5);
 hold on;
 axis([0 10 -1.5 1.5]);
 else
 if h(n+1)==0
 y=(t<n)-0*(t==n);
 else
 y=(t<n)+1*(t==n);
 end
 d=plot(t,y);title('CCCCCCCCCC');grid on;
 set(d,'LineWidth',2.5);
 hold on;
 axis([0 10 -1.5 1.5]);
 end 
 n=n+1;
 end