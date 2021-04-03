import tkinter.messagebox
from tkinter import *
from tkinter import ttk

class Resistor:

    def __init__(self, root):  # rotas de iniciação
        self.root = root
        self.root.title("Calculadora de Resistores por Código de Cores - Projeto Grupo 4N.9")  #titulo da pagina
        self.root.geometry("1352x652+0+0")    # posição na tela
        self.root.configure(background="powder blue")     # tela maior, fundo

        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=StringVar()
        var5=IntVar()
        var6=IntVar()
        var7=IntVar()
        var8=IntVar()
        var9=IntVar()

        var1.set("")
        var2.set("")
        var3.set("")
        var4.set("")
        var5.set("")
        var6.set("")
        var7.set("")
        var8.set("")
        var9.set("")


        # Seleção Faixa 1

        def Band1_Black():
            var1.set(0)
        def Band1_Brown():
            var1.set(1)
        def Band1_Red():
            var1.set(2)
        def Band1_Orange():
            var1.set(3)
        def Band1_Yellow():
            var1.set(4)
        def Band1_Green():
            var1.set(5)
        def Band1_Blue():
            var1.set(6)
        def Band1_Violet():
            var1.set(7)
        def Band1_Gray():
            var1.set(8)
        def Band1_White():
            var1.set(9)

        # Seleção Faixa 2

        def Band2_Black():
            var2.set(0)
        def Band2_Brown():
            var2.set(1)
        def Band2_Red():
            var2.set(2)
        def Band2_Orange():
            var2.set(3)
        def Band2_Yellow():
            var2.set(4)
        def Band2_Green():
            var2.set(5)
        def Band2_Blue():
            var2.set(6)
        def Band2_Violet():
            var2.set(7)
        def Band2_Gray():
            var2.set(8)
        def Band2_White():
            var2.set(9)

        #Multiplicadores

        def Multiplier_Black():
            var3.set(1)
        def Multiplier_Brown():
            var3.set(10)
        def Multiplier_Red():
            var3.set(100)
        def Multiplier_Orange():
            var3.set(1000)
        def Multiplier_Yellow():
            var3.set(10000)
        def Multiplier_Green():
            var3.set(100000)
        def Multiplier_Blue():
            var3.set(1000000)
        def Multiplier_Violet():
            var3.set(10000000)
        def Multiplier_Gray():
            var3.set(100000000)
        def Multiplier_White():
            var3.set(1000000000)

        # Tolerancia

        def Tolerance_Gold():
            var4.set(0.05)
        def Tolerance_Silver():
            var4.set(0.1)
        def Tolerance_None():
            var4.set(0.2)

        # Botão Sair
        def iExit():
            iExit = tkinter.messagebox.askyesno("Calculadora de Resistor por código de cor","Realmente deseja sair?")
            if iExit > 0:
                root.destroy()
                return

        # Botão Reiniciar
        def iReset():
            iReset = tkinter.messagebox.askyesno("Calculadora de Resistor por código de cor","Realmente deseja reiniciar?")
            if iReset > 0:
                var1.set("")
                var2.set("")
                var3.set("")
                var4.set("")
                var5.set("")
                var6.set("")
                var7.set("")
                var8.set("")
                var9.set("")
                return

        # Botão Calcular
        def CalculateResistor():
            var9= "%d%d" % ((var1.get(),var2.get()))
            t= float(var9)               #calculadora
            m= float(var3.get())         #multiplicador var/faixa3
            s= float(var4.get())         #tolerancia va/faixar4

            #====== Tolerancia faixa Gold 5% =====
            if (s == 0.05):
                q= ((t * m) /1000) * 0.05
                a= (q)
                var5.set(str('%.1f'% (a)))      #var5 é a var Divisorby1000
                var6.set(str('%.1f'% (t)+'k ohm'))      #var6 valor de resistor
                var7.set(str('%.1f'%(t - q)+'k ohm'))      #var7 valor minimo
                var8.set(str('%.1f' % (t + q) +'k ohm'))    #var8 valor maximo

            # ====== Tolerancia faixa Silver 10% =====
            elif (s == 0.1):
                q= ((t * m) /1000) * 0.1
                a= (q)
                var5.set(str('%.1f'% (a)))      #var5 é a var Divisorby1000
                var6.set(str('%.1f'% (t)+'k ohm'))      #var6 valor de resistor
                var7.set(str('%.1f'%(t - q)+'k ohm'))      #var7 valor minimo
                var8.set(str('%.1f' % (t + q) +'k ohm'))    #var8 valor maximo

            # ====== Tolerancia faixa None 20% =====
            elif (s == 0.2):
                q= ((t * m) /1000) * 0.2
                a= (q)
                var5.set(str('%.1f'% (a)))      #var5 é a var Divisorby1000
                var6.set(str('%.1f'% (t)+'k ohm'))      #var6 valor de resistor
                var7.set(str('%.1f'%(t - q)+'k ohm'))      #var7 valor minimo
                var8.set(str('%.1f' % (t + q) +'k ohm'))    #var8 valor maximo

        mainFrame= Frame(self.root,bg = 'powder blue')
        mainFrame.grid()

        TitleFrame = Frame(mainFrame, bd=10, width= 800, padx= 20, bg = 'powder blue', relief= RIDGE)  # medidas da posicao da caixa com texto
        TitleFrame.grid(row=0, column=0, columnspan=2)
        self.lblTitle = Label(TitleFrame, font=('arial' ,36, 'bold'),text = "Calculadora de Resistor por Código de Cor", bg = 'powder blue',padx=120)   # nome calculadora
        self.lblTitle.grid()
        ResistorFrame = Frame(mainFrame, bd=10, width=1200, padx=6,bg = 'powder blue', relief=RIDGE) #posicao na tela
        ResistorFrame.grid(row=1, column=0, sticky=W)

        #criando uma segunda coluna na tela

        IndicatorFrame = Frame(mainFrame, bd=10, width=1200, padx=18, bg = 'powder blue', relief=RIDGE)  # posicao na tela
        IndicatorFrame.grid(row=1, column=1, sticky=W)


        #Titulo Faixa de cor

        self.lblTitle = Label(ResistorFrame, font=('arial', 12, 'bold'),bg = 'powder blue', text="1º Faixa")
        self.lblTitle.grid(row=0, column=0)
        self.lblTitle = Label(ResistorFrame, font=('arial', 12, 'bold'),bg = 'powder blue', text="2º Faixa")
        self.lblTitle.grid(row=0, column=1)
        self.lblTitle = Label(ResistorFrame, font=('arial', 12, 'bold'),bg = 'powder blue', text="Multiplicador")
        self.lblTitle.grid(row=0, column=2)
        self.lblTitle = Label(ResistorFrame, font=('arial', 12, 'bold'), bg = 'powder blue',text="Tolerância")
        self.lblTitle.grid(row=0, column=3)

        # Criação de Botões/Faixa de cores
        self.blackcolourBand1 =Button(ResistorFrame, width=17, font=('arial',14, 'bold'),text= "preto", fg='white',command= Band1_Black,bg='black')   #esta dentro de resistor frame, fg = fontground color, bg= background color
        self.blackcolourBand1.grid(row=1, column=0)
        self.blackcolourBand2 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text="0", fg='white',command= Band2_Black,bg='black')
        self.blackcolourBand2.grid(row=1, column=1)
        self.blackcolourBand3 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text="1", fg='white',command=Multiplier_Black,bg='black')
        self.blackcolourBand3.grid(row=1, column=2)
        self.blackcolourBand4 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), fg='white',bg='black')
        self.blackcolourBand4.grid(row=1, column=3)
        #==========================================================================================================================

        self.browncolourBand1 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text="marrom", fg='black', command=Band1_Brown,bg='brown')
        self.browncolourBand1.grid(row=2, column=0)
        self.browncolourBand2 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text="1", fg='black',command= Band2_Brown,bg='brown')
        self.browncolourBand2.grid(row=2, column=1)
        self.browncolourBand3 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text="10", fg='black',command=Multiplier_Brown, bg='brown')
        self.browncolourBand3.grid(row=2, column=2)
        self.browncolourBand4 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), fg='black',bg='brown')
        self.browncolourBand4.grid(row=2, column=3)
        #==========================================================================================================================

        self.redcolourBand1 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text="vermelho", fg='black',command=Band1_Red,bg='red')
        self.redcolourBand1.grid(row=3, column=0)
        self.redcolourBand2 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text="2", fg='black',command= Band2_Red,bg='red')
        self.redcolourBand2.grid(row=3, column=1)
        self.redcolourBand3 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text="100", fg='black',command=Multiplier_Red,bg='red')
        self.redcolourBand3.grid(row=3, column=2)
        self.redcolourBand4 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), fg='black', bg='red')
        self.redcolourBand4.grid(row=3, column=3)
        # ========================================================================================================================

        self.orangecolourBand1 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text="laranja", fg='black', command=Band1_Orange,bg='orange')
        self.orangecolourBand1.grid(row=4, column=0)
        self.orangecolourBand2 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text="3", fg='black',command= Band2_Orange,bg='orange')
        self.orangecolourBand2.grid(row=4, column=1)
        self.orangecolourBand3 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text="1000", fg='black',command=Multiplier_Orange,bg='orange')
        self.orangecolourBand3.grid(row=4, column=2)
        self.orangecolourBand4 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), fg='black', bg='orange')
        self.orangecolourBand4.grid(row=4, column=3)
        # ============================================================================================================================

        self.yellowcolourBand1 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text="amarelo", fg='black',command=Band1_Yellow,bg='yellow')
        self.yellowcolourBand1.grid(row=5, column=0)
        self.yellowcolourBand2 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text="4", fg='black',command= Band2_Yellow,bg='yellow')
        self.yellowcolourBand2.grid(row=5, column=1)
        self.yellowcolourBand3 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text="10000", fg='black',command=Multiplier_Yellow,bg='yellow')
        self.yellowcolourBand3.grid(row=5, column=2)
        self.yellowcolourBand4 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), fg='black', bg='yellow')
        self.yellowcolourBand4.grid(row=5, column=3)
        # ============================================================================================================================

        self.greencolourBand1 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text="verde", fg='black',command=Band1_Green,bg='green')
        self.greencolourBand1.grid(row=6, column=0)
        self.greencolourBand2 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text="5", fg='black',command= Band2_Green,bg='green')
        self.greencolourBand2.grid(row=6, column=1)
        self.greencolourBand3 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text="100000", fg='black',command=Multiplier_Green,bg='green')
        self.greencolourBand3.grid(row=6, column=2)
        self.greencolourBand4 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), fg='black', bg='green')
        self.greencolourBand4.grid(row=6, column=3)
        # ===========================================================================================================================

        self.bluecolourBand1 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text="azul", fg='black',command=Band1_Blue,bg='blue')
        self.bluecolourBand1.grid(row=7, column=0)
        self.bluecolourBand2 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text="6", fg='black',command= Band2_Blue,bg='blue')
        self.bluecolourBand2.grid(row=7, column=1)
        self.bluecolourBand3 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text="1000000", fg='black',command=Multiplier_Blue,bg='blue')
        self.bluecolourBand3.grid(row=7, column=2)
        self.bluecolourBand4 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), fg='black', bg='blue')
        self.bluecolourBand4.grid(row=7, column=3)
        # ===========================================================================================================================

        self.violetcolourBand1 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text="violeta", fg='black',command=Band1_Violet,bg='violet')
        self.violetcolourBand1.grid(row=8, column=0)
        self.violetcolourBand2 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text="7", fg='black',command= Band2_Violet,bg='violet')
        self.violetcolourBand2.grid(row=8, column=1)
        self.violetcolourBand3 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text="10000000", fg='black',command=Multiplier_Violet,bg='violet')
        self.violetcolourBand3.grid(row=8, column=2)
        self.violetcolourBand4 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), fg='black', bg='violet')
        self.violetcolourBand4.grid(row=8, column=3)
        # ==========================================================================================================================

        self.graycolourBand1 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text="cinza", fg='black',command=Band1_Gray,bg='gray')
        self.graycolourBand1.grid(row=9, column=0)
        self.graycolourBand2 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text="8", fg='black',command= Band2_Gray,bg='gray')
        self.graycolourBand2.grid(row=9, column=1)
        self.graycolourBand3 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text= "100000000", fg='black', command=Multiplier_Gray,bg='gray')
        self.graycolourBand3.grid(row=9, column=2)
        self.graycolourBand4 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), fg='black', bg='gray')
        self.graycolourBand4.grid(row=9, column=3)
        # ==========================================================================================================================

        self.whitecolourBand1 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text="branco", fg='black',command=Band1_White,bg='white')
        self.whitecolourBand1.grid(row=10, column=0)
        self.whitecolourBand2 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text="9", fg='black',command= Band2_White,bg='white')
        self.whitecolourBand2.grid(row=10, column=1)
        self.whitecolourBand3 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text="1000000000", fg='black',command=Multiplier_White,bg='white')
        self.whitecolourBand3.grid(row=10, column=2)
        self.whitecolourBand4 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), fg='black', bg='white')
        self.whitecolourBand4.grid(row=10, column=3)
        # ===========================================================================================================================

        self.goldcolourBand1 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text="dourado", fg='black',command=Tolerance_Gold,bg='gold')
        self.goldcolourBand1.grid(row=11, column=0)
        self.goldcolourBand2 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text="", fg='black',bg='gold')
        self.goldcolourBand2.grid(row=11, column=1)
        self.goldcolourBand3 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text="0.1", fg='black', bg='gold')
        self.goldcolourBand3.grid(row=11, column=2)
        self.goldcolourBand4 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text='5%', fg='black', command=Tolerance_Gold,bg='gold')
        self.goldcolourBand4.grid(row=11, column=3)
        # ===========================================================================================================================

        self.silvercolourBand1 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text="prateado", fg='black',command=Tolerance_Silver,bg='silver')
        self.silvercolourBand1.grid(row=12, column=0)
        self.silvercolourBand2 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text="", fg='black',bg='silver')
        self.silvercolourBand2.grid(row=12, column=1)
        self.silvercolourBand3 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), fg='black',bg='silver')
        self.silvercolourBand3.grid(row=12, column=2)
        self.silvercolourBand4 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text='10%', fg='black',command=Tolerance_Silver,bg='silver')
        self.silvercolourBand4.grid(row=12, column=3)
        # ===========================================================================================================================

        self.None1 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text="none",fg='black',command=Tolerance_None,bg='white')
        self.None1.grid(row=13, column=0)
        self.None2 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text="", fg='black',bg='white')
        self.None2.grid(row=13, column=1)
        self.None3 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), fg='black', bg='white')
        self.None3.grid(row=13, column=2)
        self.None4 = Button(ResistorFrame, width=17, font=('arial', 14, 'bold'), text='20%', fg='black',command=Tolerance_None,bg='white')
        self.None4.grid(row=13, column=3)
        # ================================================IndicatorFrame===========================================================================

        # Caixa 1 indicação de faixa
        self.lblFirst = Label(IndicatorFrame, font=('arial', 12, 'bold'),bg = 'powder blue', text="1º Faixa")
        self.lblFirst.grid(row=0, column=0, sticky=W,pady=8)
        self.txtFirst = Entry(IndicatorFrame, font=('arial', 12, 'bold'), width=24,textvariable=var1)
        self.txtFirst.grid(row=0, column=1,pady=10,columnspan=3)
        self.lblSecond = Label(IndicatorFrame, font=('arial', 12, 'bold'),bg = 'powder blue', text="2º Faixa")
        self.lblSecond.grid(row=1, column=0, sticky=W,pady=8)
        self.txtSecond = Entry(IndicatorFrame, font=('arial', 12, 'bold'), width=24,textvariable=var2)
        self.txtSecond.grid(row=1, column=1,pady=10,columnspan=3)

        # Caixa 2 calculo

        self.lblMultiplier = Label(IndicatorFrame, font=('arial', 12, 'bold'), bg = 'powder blue',text="Multiplicador")
        self.lblMultiplier.grid(row=2, column=0, sticky=W,pady=8)
        self.txtMultiplier = Entry(IndicatorFrame, font=('arial', 12, 'bold'), width=24,textvariable=var3)
        self.txtMultiplier.grid(row=2, column=1,pady=10,columnspan=3)
        self.lblTolerance = Label(IndicatorFrame, font=('arial', 12, 'bold'), bg='powder blue', text="Tolerância")
        self.lblTolerance.grid(row=3, column=0, sticky=W, pady=8)
        self.txtTolerance = Entry(IndicatorFrame, font=('arial', 12, 'bold'), width=24, textvariable=var4)
        self.txtTolerance.grid(row=3, column=1, pady=10, columnspan=3)

        #Divisor

        self.lblDivideBy1000 = Label(IndicatorFrame, font=('arial', 12, 'bold'), bg = 'powder blue',text="Divisor por 1000")
        self.lblDivideBy1000.grid(row=4, column=0, sticky=W,pady=8)
        self.txtDivideBy1000 = Entry(IndicatorFrame, font=('arial', 12, 'bold'), width=24,textvariable=var5)
        self.txtDivideBy1000.grid(row=4, column=1,pady=10,columnspan=3)

        # Valor de resistor
        self.lblResistorValue = Label(IndicatorFrame, font=('arial', 12, 'bold'), bg = 'powder blue',text="Valor Resistor")
        self.lblResistorValue.grid(row=5, column=0, sticky=W, pady=8)
        self.txtResistorValue = Entry(IndicatorFrame, font=('arial', 12, 'bold'), width=24,textvariable=var6)
        self.txtResistorValue.grid(row=5, column=1,pady=10,padx=4,columnspan=3)

        # Valores minimo e maximo

        self.lblMinRange = Label(IndicatorFrame, font=('arial', 12, 'bold'), bg = 'powder blue',text="Valor Min.")
        self.lblMinRange.grid(row=6, column=0, sticky=W, pady=8)
        self.txtMinRange = Entry(IndicatorFrame, font=('arial', 12, 'bold'), width=24,textvariable=var7)
        self.txtMinRange.grid(row=6, column=1, pady=10,padx=4,columnspan=3)
        self.lblMaxRange = Label(IndicatorFrame, font=('arial', 12, 'bold'), bg = 'powder blue',text="Valor Max.")
        self.lblMaxRange.grid(row=7, column=0, sticky=W, pady=8)
        self.txtMaxRange = Entry(IndicatorFrame, font=('arial', 12, 'bold'), width=24,textvariable=var8)
        self.txtMaxRange.grid(row=7, column=1, pady=10,padx=4,columnspan=3)

        # Calculadora

        Calculate=Button(IndicatorFrame, font=('arial', 12, 'bold'), text="Calcular", width=8,command=CalculateResistor,height=2)
        Calculate.grid(row=8, column=0, pady=8)
        Calculate = Button(IndicatorFrame, font=('arial', 12, 'bold'), text="Reiniciar",width=8,command= iReset,height=2)
        Calculate.grid(row=8, column=1, pady=8)
        Calculate = Button(IndicatorFrame, font=('arial', 12, 'bold'), text="Sair",width=8,command= iExit,height=2)
        Calculate.grid(row=8, column=2, pady=8)

if __name__== '__main__':
    root = Tk()
    application = Resistor(root)
    root.mainloop()






















