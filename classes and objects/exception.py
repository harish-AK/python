def fun():
    try:
        10/0
    except Exception as e:
        print(str(e)," invalid")
    finally:
        print("program conatains error")
fun()