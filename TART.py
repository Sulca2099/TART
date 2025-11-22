import random as ra
class person():
    def __init__(self,name,myfeel=50,theirfeel=50):
        self.myfeel=myfeel
        self.theirfeel=theirfeel
        self.name=name
    
print("TART,\nTemplete\nAnd\nRandom\nTokens\nCan't write your essay, just a baby chatbot, search up ELIZA or PARRY")
userinfo=[]
respos=""
cu=0
met=False
words=[["rubber","sand,","food","camera"]]
#objects,jobs,people,aniamals,places,cool things,regular verbs
whatwords=[["nice","fun","caring","cool","smart","goat","tough"],["mean","stupid","coward","bully","weird","annoying","donut","bad"]]
#kind, mean, sad, happy
quco=0
while True:
    prompt=input("talk to tart: ")
    tokens=prompt.lower().split()
    
    if "name" in tokens:#hi my hi my name  
        if tokens.index("is")-tokens.index("name")==1 and len(tokens)-1!=tokens.index("is"):
           #print("in")
            known=False
            cu=0
            if userinfo!=[]:
                for i in userinfo:
                    cu+=1
                    if i.name==tokens[tokens.index("is")+1]:
                        known=True
                        cu-=1
            if not known:
                userinfo.append(person(tokens[tokens.index("is")+1],50,50))
                cu=len(userinfo)-1
            met=True
            respos="Ok!"
    elif "hi" in tokens and userinfo!=[]:
        respos="Hi,"+userinfo[cu][0]
    elif "hi" in tokens and userinfo==[] and not met:
        respos="Hi,\nIn order to have a converstation I need to know your name."
    elif "are" in tokens:
        if "you" in tokens:
            if tokens.index("you")<tokens.index("are"):
                if tokens[tokens.index("are")]!=len(tokens)-1 and tokens[tokens.index("are")+1]=="a":
                    getw=tokens[tokens.index("are")+2]
                else:
                    getw=tokens[tokens.index("are")+1]
                if getw in whatwords[0]:
                    respos=ra.choice(["you are "+ra.choice(whatwords[0]),"thanks!","because of you I might not take over the world!"])
                    if userinfo==[]:
                        respos="Thank you, by the way what is you name"
                        quco=345
                if getw in whatwords[1]:
                    respos=ra.choice(["you are "+ra.choice(whatwords[1]),"bruh","adolescent human!"])
    if quco==345 and len(tokens)==1:
        userinfo.append([tokens[0],60])
        respos="Ok!"
        quco=0
    if quco==0:
        pass
    print(respos)
    respos="huh?"
    mat=False
    