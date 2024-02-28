import mlflow

def calculate(x,y):
    return x+y

if  __name__ == "__main__":
    x,y = 200,50
    with mlflow.start_run():
        mlflow.log_param("x",x)
        mlflow.log_param("y",y)
        result = calculate(x,y)
        mlflow.log_param("result",result)
        print("result = ",result)