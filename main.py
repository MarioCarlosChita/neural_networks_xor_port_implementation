from network  import NetWork;




input = [[0,0],[0,1],[1,0],[1,1]];
target =[[0],[1],[1], [0]];


netCore = NetWork(input , target);
netCore.Treinar();



## predicao dos valores
input = [1,0];
print(netCore.Predicao(input));
