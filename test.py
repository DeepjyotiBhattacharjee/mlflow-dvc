import mlflow
import warnings

warnings.filterwarnings("ignore")

def calculate(X,y):
    return  X / y

if __name__ == '__main__':
    with mlflow.start_run():
        X,y = 100, 200
        result = calculate(X=X,y=y)
        print(f"Here is my result : {result}")
        mlflow.log_param("X",X)
        mlflow.log_param("y",y) 
        mlflow.log_param("result",result)