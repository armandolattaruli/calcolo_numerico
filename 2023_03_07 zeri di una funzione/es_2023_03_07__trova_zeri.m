function [alpha, it]=es_2023_03_07(f, a, b, tol, itmax)
% METODO DELLE SUCCESSIVE BISEZIONI 
% Sintassi:
%     [alpha, it] = bisezioni(f, a, b, tol, itmax)
% help 
% Parametri di input
%     f: funzione di cui cercare uno zero
%     [a, b]: intervallo di lavoro
%     tol: precisione richiesta
%     itmax: numero massimo di iterate consetite
% 
% Parametri di output
%     alpha: approsimazione di uno zero di f
%     it: numero di iterate consentite

fa=f(a);
fb=f(b);

if fa*fb>0
       error("La funzione non cambia segno agli estremi dell'intervallo.\n")
end

it=0; %contatore di iterate
while b-a>tol && it<itmax           %condizioni: finchè b-a non raggiunge la precisione e it deve essere uguale alle iterate massime
    it=it+1;
    c=(a+b)/2;
    fc=f(c);
    if fc==0
        break
    elseif fa*fc<0
        b=c;
    else 
        a=c;
        fa=fc;
    end

end
alpha=c;

if b-a>tol
       warning("precisione non raggiunta")
end


