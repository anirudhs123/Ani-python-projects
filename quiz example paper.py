from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets

w1=widgets.ToggleButton(
    value=False,
    description='INDIA',
    disabled=False,
    button_style="info", # 'success', 'info', 'warning', 'danger' or ''
    tooltip='',
    icon=''
)
w2=widgets.ToggleButton(
    value=False,
    description='AUSTRALIA',
    disabled=False,
    button_style="info", # 'success', 'info', 'warning', 'danger' or ''
    tooltip='',
    icon=''
)
w3=widgets.ToggleButton(
    value=False,
    description='ENGLAND',
    disabled=False,
    button_style="info", # 'success', 'info', 'warning', 'danger' or ''
    tooltip='',
    icon=''
)
w4=widgets.ToggleButton(
    value=False,
    description='NEW ZEALAND',
    disabled=False,
    button_style="info", # 'success', 'info', 'warning', 'danger' or ''
    tooltip='',
    icon=''
)




b1=widgets.ToggleButton(
    value=False,
    description="CN RAO",
    disabled=False,
    button_style="info", # 'success', 'info', 'warning', 'danger' or ''
    tooltip='',
    icon=''
)
b2=widgets.ToggleButton(
    value=False,
    description='MANJUL BHARGAVA',
    disabled=False,
    button_style="info", # 'success', 'info', 'warning', 'danger' or ''
    tooltip='',
    icon=''
)
b3=widgets.ToggleButton(
    value=False,
    description='AMARTYA SEN',
    disabled=False,
    button_style="info", # 'success', 'info', 'warning', 'danger' or ''
    tooltip='',
    icon=''
)
b4=widgets.ToggleButton(
    value=False,
    description='SIR CV RAMAN',
    disabled=False,
    button_style="info", # 'success', 'info', 'warning', 'danger' or ''
    tooltip='',
    icon=''
)


c1=widgets.ToggleButton(
    value=False,
    description="DUBLIN",
    disabled=False,
    button_style="info", # 'success', 'info', 'warning', 'danger' or ''
    tooltip='',
    icon=''
)
c2=widgets.ToggleButton(
    value=False,
    description='HELSINKI',
    disabled=False,
    button_style="info", # 'success', 'info', 'warning', 'danger' or ''
    tooltip='',
    icon=''
)
c3=widgets.ToggleButton(
    value=False,
    description='OSLO',
    disabled=False,
    button_style="info", # 'success', 'info', 'warning', 'danger' or ''
    tooltip='',
    icon=''
)
c4=widgets.ToggleButton(
    value=False,
    description='COPPENHAGGEN',
    disabled=False,
    button_style="info", # 'success', 'info', 'warning', 'danger' or ''
    tooltip='',
    icon=''
)


d1=widgets.ToggleButton(
    value=False,
    description="BCCI",
    disabled=False,
    button_style="info", # 'success', 'info', 'warning', 'danger' or ''
    tooltip='',
    icon=''
)
d2=widgets.ToggleButton(
    value=False,
    description='SHELL LIMITED',
    disabled=False,
    button_style="info", # 'success', 'info', 'warning', 'danger' or ''
    tooltip='',
    icon=''
)
d3=widgets.ToggleButton(
    value=False,
    description='ONGC',
    disabled=False,
    button_style="info", # 'success', 'info', 'warning', 'danger' or ''
    tooltip='',
    icon=''
)
d4=widgets.ToggleButton(
    value=False,
    description='KISSAN JAM',
    disabled=False,
    button_style="info", # 'success', 'info', 'warning', 'danger' or ''
    tooltip='',
    icon=''
)



e1=widgets.ToggleButton(
    value=False,
    description="GLEN MCGRATH",
    disabled=False,
    button_style="info", # 'success', 'info', 'warning', 'danger' or ''
    tooltip='',
    icon=''
)
e2=widgets.ToggleButton(
    value=False,
    description='MUTIAH MURALIDHARAN',
    disabled=False,
    button_style="info", # 'success', 'info', 'warning', 'danger' or ''
    tooltip='',
    icon=''
)
e3=widgets.ToggleButton(
    value=False,
    description='MITCHELL STARC',
    disabled=False,
    button_style="info", # 'success', 'info', 'warning', 'danger' or ''
    tooltip='',
    icon=''
)
e4=widgets.ToggleButton(
    value=False,
    description='LASITH MALINGA',
    disabled=False,
    button_style="info", # 'success', 'info', 'warning', 'danger' or ''
    tooltip='',
    icon=''
)


from IPython.display import clear_output
playing=True
global score
score1=0






q=widgets.Textarea(
    value='Which country won the world cup in 1983 ?',
    placeholder='Type something',
    description='QUESTION 1',
    disabled=False
)
display(q)
display(w1)
display(w2)
display(w3)
display(w4)

if(w1.value==True and w2.value==False and w3.value==False and w4.value==False and playing):
        w1.button_style='success'
        print("CORRECT ANSWER")
        
        score1=score1+1
        #print(" YOUR SCORE IS {}".format(score))
        w1.value=False
        #clear_output()
        
        

        w1.disabled=True
        w2.disabled=True
        w3.disabled=True
        w4.disabled=True
        playing=False
       
        
elif(w1.value==False and w2.value==True and w3.value==False and w4.value==False and playing):
        w1.button_style='success'
        w2.button_style='danger'
        print("WRONG ANSWER")
        
        score1=score1+0
        #print(" YOUR SCORE IS {}".format(score))
        w2.value=False
        #clear_output()
        
        w1.disabled=True
        w2.disabled=True
        w3.disabled=True
        w4.disabled=True
        
        playing=False
        
        
elif(w1.value==False and w2.value==False and w3.value==True and w4.value==False and playing):
        w1.button_style='success'
        w3.button_style='danger'
        print("WRONG ANSWER")
        
        
        score1=score1+0
        #print(" YOUR SCORE IS {}".format(score))
        w3.value=False
        #clear_output()
       
         
        w1.disabled=True
        w2.disabled=True
        w3.disabled=True
        w4.disabled=True
        playing=False
        
       
elif(w1.value==False and w2.value==False and w3.value==False and w4.value==True and playing):
        w1.button_style='success'
        w4.button_style='danger'
        print("WRONG ANSWER")
        
        
        score1=score1+0
        #print(" YOUR SCORE IS {}".format(score))
        w4.value=False
        #clear_output()
        w1.disabled=True
        w2.disabled=True
        w3.disabled=True
        w4.disabled=True
        playing=False 
        
print(" YOUR SCORE IS {}".format(score1))       
 
    
playing=True   
score2=0
q2=widgets.Textarea(
    value='Who is the first Indaian to win a fields medal ?',
    placeholder='Type something',
    description='QUESTION 2',
    disabled=False
)
display(q2)
display(b1)
display(b2)
display(b3)
display(b4)

if(b1.value==True and b2.value==False and b3.value==False and b4.value==False and playing):
        b1.button_style='danger'
        b2.button_style='success'
        print("WRONG ANSWER")
        
        score2=score2+0
        #print(" YOUR SCORE IS {}".format(score))
        w1.value=False
        #clear_output()
        
        

        b1.disabled=True
        b2.disabled=True
        b3.disabled=True
        b4.disabled=True
        playing=False
       
        
elif(b1.value==False and b2.value==True and b3.value==False and b4.value==False and playing):
        b2.button_style='success'
        
        print("CORRECT ANSWER")
        
        score2+=1
        #print(" YOUR SCORE IS {}".format(score))
        b2.value=False
        #clear_output()
        
        b1.disabled=True
        b2.disabled=True
        b3.disabled=True
        b4.disabled=True
        
        playing=False
        
        
elif(b1.value==False and b2.value==False and b3.value==True and b4.value==False and playing):
        b2.button_style='success'
        b3.button_style='danger'
        print("WRONG ANSWER")
        
        
        score2=score2+0
        #print(" YOUR SCORE IS {}".format(score))
        b3.value=False
        #clear_output()
       
         
        b1.disabled=True
        b2.disabled=True
        b3.disabled=True
        b4.disabled=True
        playing=False
        
       
elif(b1.value==False and b2.value==False and b3.value==False and b4.value==True and playing):
        b2.button_style='success'
        b4.button_style='danger'
        print("WRONG ANSWER")
        
        
        score2=score2+0
        #print(" YOUR SCORE IS {}".format(score))
        b4.value=False
        #clear_output()
        b1.disabled=True
        b2.disabled=True
        b3.disabled=True
        b4.disabled=True
        playing=False 
           
print(" YOUR SCORE IS {}".format(score1+score2))
            
playing=True  
score3=0
q3=widgets.Textarea(
    value='What is the capital of IRELAND  ?',
    placeholder='Type something',
    description='QUESTION 3',
    disabled=False
)
display(q3)
display(c1)
display(c2)
display(c3)
display(c4)

if(c1.value==True and c2.value==False and c3.value==False and c4.value==False and playing):
        c1.button_style='success'
        print("CORRECT ANSWER")
        
        score3=score3+1
        #print(" YOUR SCORE IS {}".format(score))
        c1.value=False
        #clear_output()
        
        

        c1.disabled=True
        c2.disabled=True
        c3.disabled=True
        c4.disabled=True
        playing=False
       
        
elif(c1.value==False and c2.value==True and c3.value==False and c4.value==False and playing):
        c1.button_style='success'
        c2.button_style='danger'
        print("WRONG ANSWER")
        
        score3=score3+0
        #print(" YOUR SCORE IS {}".format(score))
        c2.value=False
        #clear_output()
        
        c1.disabled=True
        c2.disabled=True
        c3.disabled=True
        c4.disabled=True
        
        playing=False
        
        
elif(c1.value==False and c2.value==False and c3.value==True and c4.value==False and playing):
        c1.button_style='success'
        c3.button_style='danger'
        print("WRONG ANSWER")
        
        
        score3=score3+0
        #print(" YOUR SCORE IS {}".format(score))
        c3.value=False
        #clear_output()
       
         
        c1.disabled=True
        c2.disabled=True
        c3.disabled=True
        c4.disabled=True
        playing=False
        
       
elif(c1.value==False and c2.value==False and c3.value==False and c4.value==True and playing):
        c1.button_style='success'
        c4.button_style='danger'
        print("WRONG ANSWER")
        
        
        score3=score3+0
        #print(" YOUR SCORE IS {}".format(score))
        c4.value=False
        #clear_output()
        c1.disabled=True
        c2.disabled=True
        c3.disabled=True
        c4.disabled=True
        playing=False 
        
print(" YOUR SCORE IS {}".format(score1+score2+score3))

playing=True
score4=0
q4=widgets.Textarea(
    value="Which company did Rahul Dravid's father worked in  ?",
    placeholder='Type something',
    description='QUESTION 4',
    disabled=False
)
display(q4)
display(d1)
display(d2)
display(d3)
display(d4)

if(d1.value==True and d2.value==False and d3.value==False and d4.value==False and playing):
        d4.button_style='success'
        d1.button_style='danger'
        print("WRONG ANSWER")
        
        score4=score4+0
        #print(" YOUR SCORE IS {}".format(score))
        d1.value=False
        #clear_output()
        
        

        d1.disabled=True
        d2.disabled=True
        d3.disabled=True
        d4.disabled=True
        playing=False
       
        
elif(d1.value==False and d2.value==True and d3.value==False and d4.value==False and playing):
        d4.button_style='success'
        d2.button_style='danger'
        print("WRONG ANSWER")
        
        score4=score4+0
        #print(" YOUR SCORE IS {}".format(score))
        d2.value=False
        #clear_output()
        
        d1.disabled=True
        d2.disabled=True
        d3.disabled=True
        d4.disabled=True
        
        playing=False
        
        
elif(d1.value==False and d2.value==False and d3.value==True and d4.value==False and playing):
        d4.button_style='success'
        d3.button_style='danger'
        print("WRONG ANSWER")
        
        
        score4=score4+0
        #print(" YOUR SCORE IS {}".format(score))
        d3.value=False
        #clear_output()
       
         
        d1.disabled=True
        d2.disabled=True
        d3.disabled=True
        d4.disabled=True
        playing=False
        
       
elif(d1.value==False and d2.value==False and d3.value==False and d4.value==True and playing):
        d4.button_style='success'
        
        print("CORRECT ANSWER")
        
        
        score4=score4+1
        #print(" YOUR SCORE IS {}".format(score))
        d4.value=False
        #clear_output()
        d1.disabled=True
        d2.disabled=True
        d3.disabled=True
        d4.disabled=True
        playing=False 

        
print(" YOUR SCORE IS {}".format(score1+score2+score3+score4)) 


playing=True
score5=0
q5=widgets.Textarea(
    value='Who is the highest wicket taker in single edition of world cup ?',
    placeholder='Type something',
    description='QUESTION 5',
    disabled=False
)
display(q5)
display(e1)
display(e2)
display(e3)
display(e4)

if(e1.value==True and e2.value==False and e3.value==False and e4.value==False and playing):
        e1.button_style='danger'
        e3.button_style="success"
        print("CORRECT ANSWER")
        
        score5=score5+0
        #print(" YOUR SCORE IS {}".format(score))
        e1.value=False
        #clear_output()
        
        

        e1.disabled=True
        e2.disabled=True
        e3.disabled=True
        e4.disabled=True
        playing=False
       
        
elif(e1.value==False and e2.value==True and e3.value==False and e4.value==False and playing):
        e3.button_style='success'
        e2.button_style='danger'
        print("WRONG ANSWER")
        
        score5=score5+0
        #print(" YOUR SCORE IS {}".format(score))
        e2.value=False
        #clear_output()
        
        e1.disabled=True
        e2.disabled=True
        e3.disabled=True
        e4.disabled=True
        
        playing=False
        
        
elif(e1.value==False and e2.value==False and e3.value==True and e4.value==False and playing):
        e3.button_style='success'
        
        print("CORRECT ANSWER")
        
        
        score5=score5+1
        #print(" YOUR SCORE IS {}".format(score))
        e3.value=False
        #clear_output()
       
         
        e1.disabled=True
        e2.disabled=True
        e3.disabled=True
        e4.disabled=True
        playing=False
        
       
elif(e1.value==False and e2.value==False and e3.value==False and e4.value==True and playing):
        e3.button_style='success'
        e4.button_style='danger'
        print("WRONG ANSWER")
        
    
        score5=score5+0
        #print(" YOUR SCORE IS {}".format(score))
        e4.value=False
        #clear_output()
        e1.disabled=True
        e2.disabled=True
        e3.disabled=True
        e4.disabled=True
        playing=False 
        
print(" YOUR SCORE IS {}".format(score1+score2+score3+score4+score5))    
#print(score1)
#print(score2)
#print(score3)
          
