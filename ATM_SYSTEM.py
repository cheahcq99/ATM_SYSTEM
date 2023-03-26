#allignment
#give option3 on Transfer() for change transfer limit
#transfer() can go until (-)ve value ############       FIX      ############

import time
import datetime
import os

dt            = datetime.datetime.now()
chances       = 3
accbalance    = 15000.00
pin_num       = ()
withdrawlim   = 2000.00
transferlim   = 2000.00
thanks        = ('Thank you for using our services!\nHave a nice day!')
accnum        = ()

def Clear():
    os.system('cls')
    
#Begin
def startup():
    global accnum
    print('Welcome to XYZ bank!')
    accnum = int(input('Please enter your account number (12 integers): '))
    print('===============================================================')
    accnum1 = str(accnum)
    if len(accnum1) == 12:
        accnum = accnum1
        print('Loading... ...')
        time.sleep(2)
        pin()
    else:
        print('Please enter ONLY 12 integers for your account number. Thank you.')
        print('Returning to start-up page.')
        print('===============================================================')
        print('Returning... ...')
        time.sleep(2)
        Clear()
        startup()

#pin number function
def pin():
    Clear()
    global pin_num
    pin_num = int(input('Please set up your 4 digit pin number as a new user: '))
    code = pin_num
    confirm = int(input('Please retype your 4 digit pin number              : '))
    print('===============================================================')
    if confirm == code:
        print('Loading... ...')
        time.sleep(2)
        Clear()
        print('Set up successfully!')
        print('===============================================================')
        print('Returning to log in page... ...')
        time.sleep(2)
        code = confirm
        pin_num = code
        login()
    else:
        print('Pin number unmatched. Please try again.\nThank you.')
        print('===============================================================')
        print('Returning... ...')        
        pin()

#login function    
def login():
    Clear()
    global pin_num
    global chances
    global accnum
    print('Your account number\t\t\t:', accnum)
    userinp = int(input('Please insert your 4 digit pin number\t: '))
    print('===============================================================')
    if userinp == pin_num:
        print('Loading... ...')
        time.sleep(2)
        Clear()
        print('Log in successfully!')
        time.sleep(2)
        print('===============================================================')
        print('Loading... ...')
        time.sleep(2)
        showlist()
    else:
        chances = chances - 1
        if chances == 2:
            print('Incorrect pin number. 2 more chances remaining.')
            print('Please try again. Thank you.')
            print('===============================================================')
            print('Returning to log in page... ...')
            time.sleep(2)
            login()
        if chances == 1:
            print('Incorrect pin number. 1 more chance remaining.')
            print('Please try again. Thank you.')
            print('===============================================================')
            print('Returning to log in page... ...')
            time.sleep(2)
            login()
        if chances == 0:
            print('Pin number key in wrongly for 3 times.\nFailed to log in.')
            print('Thank you for using our services!\nHave a nice day!')
            print('===============================================================')
            print('Leaving... ...')
            time.sleep(2)
            exit()

#select list
def showlist():
    Clear()
    print('Enter the number of action you wish to perform.(1-9, 0 for EXIT)')
    print('\t[1] Check Balance')
    print('\t[2] Withdraw Money')
    print('\t[3] Deposit Money')
    print('\t[4] Transfer Money')
    print('\t[5] Mobile Top-Up')
    print('\t[6] Change Pin Number')
    print('\t[7] Print Mini Statement')
    print('\t[8] Pay Bills')
    print('\t[9] Overseas Usage')
    print('\t[0] EXIT')
    print('===============================================================')
    Sel()

#user selection function    
def Sel():
    usersel = int(input('Which action you wish to perform? (1-9, 0 for EXIT): '))
    if usersel == 1:
        print('Loading... ...')
        time.sleep(2)
        CheckBal()
    elif usersel == 2:
        print('Loading... ...')
        time.sleep(2)
        Withdraw()
    elif usersel == 3:
        print('Loading... ...')
        time.sleep(2)
        Deposit()
    elif usersel == 4:
        print('Loading... ...')
        time.sleep(2)
        Transfer()
    elif usersel == 5:
        print('Loading... ...')
        time.sleep(2)
        MobileTopUp()
    elif usersel == 6:
        print('Loading... ...')
        time.sleep(2)
        ChangePin()
    elif usersel == 7:
        print('Loading... ...')
        time.sleep(2)
        MiniStat()
    elif usersel == 8:
        print('Loading... ...')
        time.sleep(2)
        Bills()
    elif usersel == 9:
        print('Loading... ...')
        time.sleep(2)
        Overseas()
    elif usersel == 0:
        print('Loading... ...')
        time.sleep(2)
        Shutdown()
    else:
        print('Please insert ONLY the option given. (1-9, 0 for EXIT)')
        print('===============================================================')
        print('Returning... ...')
        showlist()
        

#continue or exit function
def UserOpt():
    Clear()
    print('\t[1] Yes\n\t[2] No')
    usersel = input('Would you like to perform other action? (1/2): ')
    print('===============================================================')
    if usersel == '1':
        print('Loading... ...')
        time.sleep(2)
        showlist()
    elif usersel == '2':
        Shutdown()
    else:
        print('Request DENIED.\nPlease insert ONLY the option given (1/2).\nThank you.')
        print('Returning... ...')
        UserOpt()

#balance checking
def CheckBal():
    Clear()
    global accbalance
    print('Your current account balance is: RM', accbalance)
    print('===============================================================')
    UserOpt()

#withdraw function
def Withdraw():
    Clear()
    global accbalance
    global withdrawlim
    WLim = int(withdrawlim)
    print('Your current account balance\t: RM', accbalance)
    print('This ATM only allow withdrawal with RM 10, RM 20, RM 50, RM 100 notes.')
    usersel = int(input('How much would you wish to withdraw\t: RM '))
    print('===============================================================')
    if (usersel > WLim):
        print('Loading... ...')
        time.sleep(2)
        print('Your withdraw amount exceed your current withdraw limit.')
        WithdrawLim()
    elif usersel == 0 or usersel < 0:
        print('Unavailable amount entered.\nReturning to home page.')
        print('===============================================================')
        print('Returning... ...')
        time.sleep(2)
        showlist()
    else:
        if (accbalance - 10)<usersel:
            print('Insufficient amount.\nMinimum of RM 10 is required in your bank account')
            print('===============================================================')
            print('Loading... ...')
            time.sleep(2)
            WithdrawOpt()
        else:
            print('The amount entered is RM', usersel)
            print('===============================================================')
            print('Loading... ...')
            time.sleep(2)
            Clear()
            statement = print('The amount you wish to withdraw\t: RM',usersel)
            print('\t[1] Yes\n\t[2] No')
            confirm = input('Confirm? (1/2)\t\t: ')
            print('===============================================================')
            if confirm == '1':
                Clear()
                print('Loading... ...')
                time.sleep(2)
                print('Withdraw success!')
                print('===============================================================')
                print('Withdraw amount: RM', usersel)
                accbalance = accbalance - usersel
                print('Your new account balance\t: RM', accbalance)
                print('Transaction Date/Time: ',(dt.strftime("%x")),(dt.strftime("%X")))
                UserOpt()
            elif confirm == '2':
                WithdrawOpt()
            else:
                print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
                print('===============================================================')
                print('Loading... ...')
                time.sleep(2)
                Withdraw()

#limitation for withdraw
def WithdrawLim():
    Clear()
    global withdrawlim
    WLim = withdrawlim
    print('Your current withdrawal limit\t: RM', WLim)
    print('\t[1] Yes\t[2] No')
    usersel = input('Would you like to reset your withdrawal limit? (1/2)\t: ')
    print('===============================================================')
    if usersel == '1':
        Clear()
        print('Loading... ...')
        time.sleep(2)
        print('===============================================================')
        reset = int(input('Please insert the new withdrawal limit\t: RM '))
        print('Your new withdrawal limit\t\t: RM', reset)
        print('\t[1] Yes\n\t[2] No')
        usersel2 = input('Confirm your new withdrawal limit? (1/2)\t: ')
        print('===============================================================')
        if usersel2 == '1':
            WLim = reset
            withdrawlim = WLim
            Clear()
            print('Loading... ...')
            time.sleep(2)
            print('===============================================================')
            print('Set up complete.\nNew withdrawal limit\t\t: RM', withdrawlim)
            WithdrawOpt()
        elif usersel2 == '2':
            WithdrawLim()
        else:
            print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
            print('===============================================================')
            print('Returning... ...')
            time.sleep(2)
            WithdrawLim()
    elif usersel == '2':
        print('Loading... ...')
        time.sleep(2)
        Withdraw()
    else:
        print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
        print('===============================================================')
        print('Returning... ...')
        time.sleep(2)
        WithdrawLim()

        
#Repeat withdraw or exit function
def WithdrawOpt():
    Clear()
    print('\t[1] Yes\n\t[2] No')
    usersel = input('Would you wish to continue to withdraw money? (1/2)\t: ')
    print('===============================================================')
    if usersel == '1':
        print('Loading... ...')
        time.sleep(2)
        Withdraw()
    elif usersel == '2':
        UserOpt()
    else:
        print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
        print('===============================================================')
        print('Returning... ...')
        time.sleep(2)
        WithdrawOpt()

        
#Deposit function
def Deposit():
    Clear()
    global accbalance
    print('Your current account balance\t\t: RM', accbalance)
    print('This ATM only accept RM 10, RM 20, RM 50, RM 100 notes')
    usersel = int(input('Please insert the amount you wish to deposit\t: RM '))
    print('===============================================================')
    if usersel == 0 or usersel < 0:
        print('Unavailable amount entered.\nReturning to home page.')
        print('===============================================================')
        print('Returning... ...')
        time.sleep(2)
        showlist()
    else:
        print('The entered amount\t\t\t: RM', usersel)
        print('===============================================================')
        print('\t[1] Yes\n\t[2] No')
        usersel2 = input('Please confirm the deposit amount. (1/2)\t: ')
        print('===============================================================')
        statement = usersel2
        if usersel2 == '1':
            accbalance = accbalance + usersel
            print('Verifying... ...')
            time.sleep(2)
            Clear()
            print('Deposit successfully!')
            print('Deposit amount: RM', usersel)
            print('Your new account balance\t\t: RM', accbalance)
            print('Transaction Date/Time: ',(dt.strftime("%x")),(dt.strftime("%X")))
            UserOpt()
        elif usersel2 == '2':
            DepositOpt()
        else:
            print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
            print('===============================================================')
            print('Returning... ...')
            time.sleep(2)
            Deposit()

            
#Repeat deposit or exit function
def DepositOpt():
    print('Loading... ...')
    time.sleep(2)
    Clear()
    print('\t[1] Yes\n\t[2] No')
    usersel = input('Would you wish to continue to deposit money? (1/2)\t: ')
    print('===============================================================')
    if usersel == '1':
        print('Loading... ...')
        time.sleep(2)
        Deposit()
    elif usersel == '2':
        UserOpt()
    else:
        print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
        print('Returning... ...')
        time.sleep(2)
        DepositOpt()

        
#Money transfer function
def Transfer():
    Clear()
    global accbalance
    global transferlim
    print('Which bank would you wish to transfer to?')
    print('\t[1] Alliance Bank\n\t[2] Other Bank')
    usersel = input('Please select the bank you wish to transfer to (1/2)\t: ')
    print('===============================================================')
    if usersel == '1':
        print('Loading... ...')
        time.sleep(2)
        Clear()
        print('Your current account balance\t\t: RM', accbalance)
        print('Your current transfer limit\t\t: RM', transferlim)
        print('===============================================================')
        print('\t[1] Transfer money\n\t[2] Reset transfer limit')
        usersel2 = input('Please insert the action you wish to perform (1/2)\t: ')
        print('===============================================================')
        if usersel2 == '1':
            print('Loading... ...')
            time.sleep(2)
            TransferAccNum1()
        elif usersel2 == '2':
            TransferLim()
        else:
            print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
            print('===============================================================')
            print('Returning... ...')
            time.sleep(2)
            Transfer()
    elif usersel == '2':
        Clear()
        print('Loading... ...')
        time.sleep(2)
        print('RM 0.53 will be charged for this transaction.')
        print('===============================================================')
        print('\t[1] Yes\n\t[2] No')
        usersel3 = input('Do you want to continue? (1/2)\t: ')
        print('===============================================================')
        if usersel3 == '1':
            print('Loading... ...')
            time.sleep(2)
            Clear()
            print('Your current account balance\t\t: RM', accbalance)
            print('Your current transfer limit\t\t: RM', transferlim)
            print('===============================================================')
            print('\t[1] Transfer money\n\t[2] Reset transfer limit')
            usersel4 = input('Please insert the action you wish to perform (1/2)\t: ')
            print('===============================================================')
            if usersel4 == '1':
                print('Loading... ...')
                time.sleep(2)
                TransferAccNum2()
            elif usersel4 == '2':
                TransferLim()
            else:
                print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
                print('===============================================================')
                print('Returning... ...')
                time.sleep(2)
                Transfer()
        elif usersel3 == '2':
            UserOpt()
        else:
            print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
            print('===============================================================')
            print('Returning... ...')
            time.sleep(2)
            Transfer()
    else:
        print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
        print('===============================================================')
        print('Returning... ...')
        time.sleep(2)
        Transfer()

#alliance bank transfer
def TransferAccNum1():
    global accbalance
    global transferlim
    Clear()
    acc_num = int(input('Please insert the account number you wish to transfer to (15/16 integers): '))
    print('===============================================================')
    print('Loading... ...')
    time.sleep(2)
    acc_num1 = str(acc_num)
    if len(acc_num1) > 16 or len(acc_num1) < 15:
        Clear()
        print('Unavailable account number entered.')
        print('Please insert account number in between 15 to 16 integers.')
        TransferOpt()
    else:
        Clear()
        trans_amt = float(input('Please insert the amount you wish to transfer\t: RM '))
        print('===============================================================')
        stat = accbalance - trans_amt
        if stat < 10 or stat == 10:
            print('Loading... ...')
            time.sleep(2)
            Clear()
            print('Insufficient amount.')
            print('Minimum of RM 10 is required in your bank account')
            print('Returning to home page... ...')
            time.sleep(2)
            showlist()
        else:
            print('Loading... ...')
            time.sleep(2)
            Clear()
            print('Transfer account\t\t:', acc_num)
            print('Transfer amount\t\t: RM', trans_amt)
            if (trans_amt > transferlim):
                print('Loading... ...')
                time.sleep(2)
                Clear()
                print('Transfer amount exceed your transfer limit.')
                print('===============================================================')
                print('\t[1] Yes\n\t[2] No')
                usersel = input('Do you want to reset your transfer limit? (1/2)\t: ')
                print('===============================================================')
                if usersel == '1':
                    TransferLim()
                elif usersel == '2':
                    TransferOpt()
                else:
                    print('Request DENIED.\nPlease insert ONLY the option given.')
                    print('Returning... ...')
                    print('===============================================================')
                    time.sleep(2)
                    TransferAccNum1()                
            else:
                print('Loading... ...')
                time.sleep(2)
                Clear()
                print('\t[1] Yes\n\t[2] No')
                usersel2 = input('Please confirm your transfer option (1/2)\t: ')
                print('===============================================================')
                if usersel2 == '1':
                    accbalance = stat
                    print('Loading... ...')
                    time.sleep(2)
                    print('===============================================================')
                    print('RM',trans_amt,'transferred successfully to',acc_num,'!')
                    print('Your new account balance: RM', accbalance)
                    print('Transaction Date/Time: ',(dt.strftime("%x")),(dt.strftime("%X")))
                    UserOpt()
                elif usersel2 == '2':
                    TransferOpt()
                else:
                    print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
                    print('Returning... ...')
                    print('===============================================================')
                    time.sleep(2)
                    TransferAccNum1()


#other bank transaction
def TransferAccNum2():
    global accbalance
    global transferlim
    global accnum
    Clear()
    acc_num = int(input('Please insert the account number you wish to transfer to (8/10/12 integers): '))
    print('===============================================================')
    print('Loading... ...')
    time.sleep(2)
    acc_num1 = str(acc_num)
    if (acc_num1 == accnum):
        Clear()
        print('Request DENIED.')
        print('Transfer to the same account is unavailable.')
        TransferOpt()
    else:
        if len(acc_num1) == 8 or len(acc_num1) == 10 or len(acc_num1) == 12:
            print('Loading... ...')
            time.sleep(2)
            Clear()
            trans_amt = float(input('Please insert the amount you wish to transfer\t: RM '))
            print('===============================================================')
            stat = accbalance - 0.53 - trans_amt
            if stat < 10 or stat == 10:
                print('Loading... ...')
                time.sleep(2)
                Clear()
                print('Insufficient amount.')
                print('Minimum of RM 10 is required in your bank account')
                print('Returning to home page... ...')
                print('===============================================================')
                time.sleep(2)
                showlist()
            else:
                print('Loading... ...')
                time.sleep(2)
                Clear()
                print('Transfer account\t\t:', acc_num)
                print('Transfer amount\t\t: RM', trans_amt)
                if (trans_amt > transferlim):
                    print('Loading... ...')
                    time.sleep(2)
                    Clear()
                    print('Transfer amount exceed your transfer limit.')
                    print('\t[1] Yes\n\t[2] No')
                    usersel = input('Do you want to reset your transfer limit? (1/2)\t: ')
                    print('===============================================================')
                    if usersel == '1':
                        TransferLim()
                    elif usersel == '2':
                        TransferOpt()
                    else:
                        print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
                        print('Returning... ...')
                        print('===============================================================')
                        time.sleep(2)
                        TransferAccNum2()         
                else:
                    print('Loading... ...')
                    time.sleep(2)
                    Clear()
                    print('\t[1] Yes\n\t[2] No')
                    usersel2 = input('Please confirm your transfer option (1/2)\t: ')
                    print('===============================================================')
                    if usersel2 == '1':
                        accbalance = stat
                        print('Loading... ...')
                        time.sleep(2)
                        Clear()
                        print('RM',trans_amt,'transferred successfully to', acc_num,'!')
                        print('Your new account balance: RM', accbalance)
                        print('Transaction Date/Time: ',(dt.strftime("%x")),(dt.strftime("%X")))
                        UserOpt()
                    elif usersel2 == '2':
                        TransferOpt()
                    else:
                        print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
                        print('Returning... ...')
                        print('===============================================================')
                        time.sleep(2)
                        TransferAccNum2()
        else:
            print('Request DENIED.\nUnavailable account number entered.')
            print('Returning... ...')
            print('===============================================================')
            time.sleep(2)
            TransferOpt()
        

 #Limitation of tansaction               
def TransferLim():
    global transferlim
    print('Loading... ...')
    time.sleep(2)
    Clear()
    print('Your current transfer limit: RM', transferlim)
    reset = float(input('Please insert your new transfer limit\t: RM '))
    print('===============================================================')
    print('Loading... ...')
    time.sleep(2)
    print('Your new transfer limit\t\t: RM', reset)
    print('\t[1] Yes\n\t[2] No')
    usersel = input('Confirm your new transfer limit? (1/2)\t: ')
    print('===============================================================')
    if usersel == '1':
        print('Loading... ...')
        time.sleep(2)
        Clear()
        transferlim = reset
        print('Set up complete.\nNew transfer limit: RM', transferlim)
        TransferOpt()
    elif usersel == '2':
        TransferLim()
    else:
        print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
        print('Returning... ...')
        print('===============================================================')
        time.sleep(2)
        TransferLim()

#repeat transfer or exit function
def TransferOpt():
    print('Loading... ...')
    time.sleep(2)
    Clear()
    print('\t[1] Yes\n\t[2] No')
    usersel = input('Would you like to continue to transfer money? (1/2)\t: ')
    print('===============================================================')
    if usersel == '1':
        print('Loading... ...')
        time.sleep(2)
        Transfer()
    elif usersel == '2':
        UserOpt()
    else:
        print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
        print('Returning... ...')
        print('===============================================================')
        time.sleep(2)
        TransferOpt()

#top-up function
def MobileTopUp():
    Clear()
    global accbalance
    print('Please insert the phone number you wish to top-up.')
    userinp = int(input('+0'))
    print('===============================================================')
    stat1 = float(accbalance)
    stat2 = str(userinp)
    if len(stat2) == 9 or len(stat2) == 10:
        print('Loading... ...')
        time.sleep(2)
        Clear()
        print('\t[1] RM   5')
        print('\t[2] RM  10')
        print('\t[3] RM  20')
        print('\t[4] RM  50')
        print('\t[5] RM 100')
        print('\t[6] RM 150')
        print('\t[7] RM 200')
        print("\t[8] 'CANCEL'")
        print('===============================================================')
        usersel = int(input('Please select the amount you wish to top-up (1-7, 8 to CANCEL)\t: '))
        print('===============================================================')
        if usersel == 1:
            print('Loading... ...')
            time.sleep(2)
            Clear()
            print('Amount selected\t\t: RM 5')
            print('\t[1] Yes\n\t[2] No')
            usersel1 = str(input('Please confirm your top-up amount (1/2)\t: '))
            print('===============================================================')
            if usersel1 == '1':
                print('Loading... ...')
                time.sleep(2)
                Clear()
                if ((accbalance - 10) - 5) == 0 or ((accbalance - 10) - 5) <0:
                    print('Insufficient amount.\nMinimum of RM 10 is required in your bank account.')
                    TopUpOpt()
                else:
                    print('Top-up successfully to +0', userinp)
                    accbalance = accbalance - 5
                    print('Your new account balance\t: RM', accbalance)
                    print('Transaction Date/Time: ',(dt.strftime("%x")),(dt.strftime("%X")))
                    UserOpt()
            elif usersel1 == '2':
                TopUpOpt()
            else:
                print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
                print('Returning... ...')
                print('===============================================================')
                time.sleep(2)
                MobileTopUp()
        elif usersel == 2:
            Clear()
            print('Amount selected\t\t: RM 10')
            print('\t[1] Yes\n\t[2] No')
            usersel1 = str(input('Please confirm your top-up amount (1/2)\t: '))
            print('===============================================================')
            if usersel1 == '1':
                print('Loading... ...')
                time.sleep(2)
                Clear()
                if ((accbalance - 10) - 10) == 0 or ((accbalance - 10) - 10) <0:
                    print('Insufficient amount.\nMinimum of RM 10 is required in your bank account.')
                    TopUpOpt()
                else:
                    print('Top-up successfully to +0', userinp)
                    accbalance = accbalance - 10
                    print('Your new account balance\t: RM', accbalance)
                    print('Transaction Date/Time: ',(dt.strftime("%x")),(dt.strftime("%X")))
                    UserOpt()
            elif usersel1 == '2':
                TopUpOpt()
            else:
                print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
                print('Returning... ...')
                print('===============================================================')
                time.sleep(2)
                MobileTopUp()
        elif usersel == 3:
            Clear()
            print('Amount selected\t\t: RM 20')
            print('\t[1] Yes\n\t[2] No')
            usersel1 = str(input('Please confirm your top-up amount (1/2)\t: '))
            print('===============================================================')
            if usersel1 == '1':
                print('Loading... ...')
                time.sleep(2)
                Clear()
                if ((accbalance - 10) - 20) == 0 or ((accbalance - 10) - 20) <0:
                    print('Insufficient amount.\nMinimum of RM 10 is required in your bank account.')
                    TopUpOpt()
                else:
                    print('Top-up successfully to +0', userinp)
                    accbalance = accbalance - 20
                    print('Your new account balance\t: RM', accbalance)
                    print('Transaction Date/Time: ',(dt.strftime("%x")),(dt.strftime("%X")))
                    UserOpt()
            elif usersel1 == '2':
                TopUpOpt()
            else:
                print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
                print('Returning... ...')
                print('===============================================================')
                time.sleep(2)
                MobileTopUp()
        elif usersel == 4:
            Clear()
            print('Amount selected\t\t: RM 50')
            print('\t[1] Yes\n\t[2] No')
            usersel1 = str(input('Please confirm your top-up amount (1/2)\t: '))
            print('===============================================================')
            if usersel1 == '1':
                print('Loading... ...')
                time.sleep(2)
                Clear()
                if ((accbalance - 10) - 50) == 0 or ((accbalance - 10) - 50) <0:
                    print('Insufficient amount.\nMinimum of RM 10 is required in your bank account.')
                    TopUpOpt()
                else:
                    print('Top-up successfully to +0', userinp)
                    accbalance = accbalance - 50
                    print('Your new account balance\t: RM', accbalance)
                    print('Transaction Date/Time: ',(dt.strftime("%x")),(dt.strftime("%X")))
                    UserOpt()
            elif usersel1 == '2':
                TopUpOpt()
            else:
                print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
                print('Returning... ...')
                print('===============================================================')
                time.sleep(2)
                MobileTopUp()
        elif usersel == 5:
            Clear()
            print('Amount selected\t\t: RM 100')
            print('\t[1] Yes\n\t[2] No')
            usersel1 = str(input('Please confirm your top-up amount (1/2)\t: '))
            print('===============================================================')
            if usersel1 == '1':
                print('Loading... ...')
                time.sleep(2)
                Clear()
                if ((accbalance - 10) - 100) == 0 or ((accbalance - 10) - 100) <0:
                    print('Insufficient amount.\nMinimum of RM 10 is required in your bank account.')
                    TopUpOpt()
                else:
                    print('Top-up successfully to +0', userinp)
                    accbalance = accbalance - 100
                    print('Your new account balance\t: RM', accbalance)
                    print('Transaction Date/Time: ',(dt.strftime("%x")),(dt.strftime("%X")))
                    UserOpt()
            elif usersel1 == '2':
                TopUpOpt()
            else:
                print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
                print('Returning... ...')
                print('===============================================================')
                time.sleep(2)
                MobileTopUp()
        elif usersel == 6:
            Clear()
            print('Amount selected\t\t: RM 150')
            print('\t[1] Yes\n\t[2] No')
            usersel1 = str(input('Please confirm your top-up amount (1/2)\t: '))
            print('===============================================================')
            if usersel1 == '1':
                print('Loading... ...')
                time.sleep(2)
                if ((accbalance - 10) - 150) == 0 or ((accbalance - 10) - 150) <0:
                    print('Insufficient amount.\nMinimum of RM 10 is required in your bank account.')
                    TopUpOpt()
                else:
                    print('Top-up successfully to +0', userinp)
                    accbalance = accbalance - 150
                    print('Your new account balance\t: RM', accbalance)
                    print('Transaction Date/Time: ',(dt.strftime("%x")),(dt.strftime("%X")))
                    UserOpt()
            elif usersel1 == '2':
                TopUpOpt()
            else:
                print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
                print('Returning... ...')
                print('===============================================================')
                time.sleep(2)
                MobileTopUp()
        elif usersel == 7:
            Clear()
            print('Amount selected\t\t: RM 200')
            print('\t[1] Yes\n\t[2] No')
            usersel1 = str(input('Please confirm your top-up amount (1/2)\t: '))
            print('===============================================================')
            if usersel1 == '1':
                print('Loading... ...')
                time.sleep(2)
                Clear()
                if ((accbalance - 10) - 200) == 0 or ((accbalance - 10) - 200) <0:
                    print('Insufficient amount.\nMinimum of RM 10 is required in your bank account.')
                    TopUpOpt()
                else:
                    print('Top-up successfully to +0', userinp)
                    accbalance = accbalance - 200
                    print('Your new account balance\t: RM', accbalance)
                    print('Transaction Date/Time: ',(dt.strftime("%x")),(dt.strftime("%X")))
                    UserOpt()
            elif usersel1 == '2':
                TopUpOpt()
            else:
                print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
                print('Returning... ...')
                print('===============================================================')
                time.sleep(2)
                MobileTopUp()
        elif usersel == 8:
            UserOpt()
        else:
            print('Request DENIED.\nPlease insert ONLY the option given. (1-8)')
            print('Returning... ...')
            print('===============================================================')
            time.sleep(2)
            MobileTopUp()
    else:
        print('Request DENIED.\nUnavailable numbers entered.')
        print('Please insert numbers between 9 to 10 integers.')
        TopUpOpt()

#Repeat top-up or exit function
def TopUpOpt():
    print('Loading... ...')
    time.sleep(2)
    Clear()
    print('\t[1] Yes\n\t[2] No')
    usersel = input('Would you like to continue to top-up? (1/2)\t: ')
    print('===============================================================')
    if usersel == '1':
        print('Loading... ...')
        time.sleep(2)
        MobileTopUp()
    elif usersel == '2':
        UserOpt()
    else:
        print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
        print('Returning... ...')
        print('===============================================================')
        time.sleep(2)
        TopUpOpt()

#pin number changing function
def ChangePin():
    global pin_num
    ori = pin_num
    Clear()
    userinp1 = int(input('Please insert your current 4 digit pin number\t: '))
    print('===============================================================')
    print('Loading... ...')
    time.sleep(2)
    if userinp1 == ori:
        print('Pin number matched!')
        Clear()
        userinp2 = int(input('Please insert your new 4 digit pin number\t: '))
        print('===============================================================')
        stat = str(userinp2)
        print('Loading... ...')
        time.sleep(2)
        if userinp2 == userinp1:
            Clear()
            print('New pin number cannot be same as old pin number.')
            print('Returning... ...')
            print('===============================================================')
            time.sleep(2)
            ChangePinOpt()
        else:
            if len(stat) == 4:
                Clear()
                userinp3 = int(input('Please retype your new 4 digit pin number\t: '))
                print('===============================================================')
                print('Loading... ...')
                time.sleep(2)
                Clear()
                if userinp3 == userinp2:
                    print('Pin number updated!')
                    UserOpt()
                else:
                    print('Pin number unmatched!')
                    ChangePinOpt()
            else:
                print('Please insert ONLY 4 digit pin number.')
                print('Returning... ...')
                print('===============================================================')
                time.sleep(2)
                ChangePinOpt()
    else:
        print('Pin number unmatched!')
        print('Returning... ...')
        print('===============================================================')
        time.sleep(2)
        ChangePinOpt()

#Repeat pin changing or exit function       
def ChangePinOpt():
    print('Loading... ...')
    time.sleep(2)
    Clear()
    print('\t[1] Yes\n\t[2] No')
    usersel = input('Would you like to try again? (1/2)\t: ')
    print('===============================================================')
    if usersel == '1':
        print('Loading... ...')
        time.sleep(2)
        ChangePin()
    elif usersel == '2':
        UserOpt()
    else:
        print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
        print('Returning... ...')
        print('===============================================================')
        time.sleep(2)
        ChangePinOpt()

#show mini statement function
def MiniStat():
    Clear()
    global accnum
    global accbalance
    print('===============================================================')
    print('XYZ Bank Mini Statement')
    print('To Account:', accnum)
    print('===============================================================')
    print('DATE \t\tTIME')
    print((dt.strftime("%x")),'      ',(dt.strftime("%X")))
    print('===============================================================')
    print('Available balance:',accbalance)
    print('===============================================================')
    print('History Record')
    print('10/03/21 \tWithdrawal\tRM  500')
    print('15/03/21 \tWithdrawal\tRM 1000')
    print('20/03/21 \tDeposit   \tRM 1500')
    print('25/03/21 \tDeposit   \tRM 2000')
    print('30/03/21 \tWithdrawal\tRM  500')
    print('===============================================================')
    UserOpt()

#Bill payment function
def Bills():
    Clear()
    print('[1] Water Bills')
    print('[2] Electricity Bills')
    print('[3] Astro Bills')
    print('[4] Credit Card Bills')
    usersel = input('Please insert your option (1-4)\t: ')
    print('===============================================================')
    if usersel == '1':
        print('Loading... ...')
        time.sleep(2)
        print('The total amount for Water Bills: RM 30')
        BillsOpt1()        
    elif usersel == '2':
        print('Loading... ...')
        time.sleep(2)
        print('The total amount for Electricity Bills: RM 150')
        BillsOpt2()
    elif usersel == '3':
        print('Loading... ...')
        time.sleep(2)
        print('The total amount for Astro Bills: RM 250')
        BillsOpt3()
    elif usersel == '4':
        print('Loading... ...')
        time.sleep(2)
        print('The total amount for Credit Card Bills: RM 3560')
        BillsOpt4()
    else:
        print('Please insert ONLY the option given. (1-4)')
        print('Returning... ...')
        print('===============================================================')
        time.sleep(2)
        Bills()

#water bill payment function
def BillsOpt1():
    Clear()
    global accbalance
    print('\t[1] Yes\n\t[2] No')
    usersel = input('Confirm payment RM 30? (1/2)\t: ')
    print('===============================================================')
    if usersel == '1':
        print('Loading... ...')
        time.sleep(2)
        Clear()
        if ((accbalance - 10) - 30) == 0 or ((accbalance - 10) - 30) <0:
            print('Insufficient amount.\nMinimum of RM 10 is required in your bank account.')
            UserOpt()
        else:
            print('Payment success!')
            accbalance = accbalance - 30
            print('Your new account balance\t: RM', accbalance)
            print('Transaction Date/Time: ',(dt.strftime("%x")),(dt.strftime("%X")))
            UserOpt()
    elif usersel == '2':
        print('Loading... ...')
        time.sleep(2)
        Clear()
        print('\t[1] Yes\n\t[2] No')
        usersel2 = input('Would you wish to continue to bills payment? (1/2)\t: ')
        print('===============================================================')
        if usersel2 == '1':
            print('Loading... ...')
            time.sleep(2)
            Bills()
        elif usersel2 == '2':
            UserOpt()
        else:
            print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
            print('Returning... ...')
            print('===============================================================')
            time.sleep(2)
            BillsOpt1()
    else:
        print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
        print('Returning... ...')
        print('===============================================================')
        time.sleep(2)
        BillsOpt1()

#Electricity bill payment function       
def BillsOpt2():
    global accbalance
    Clear()
    print('\t[1] Yes\n\t[2] No')
    usersel = input('Confirm payment RM 150? (1/2)\t: ')
    print('===============================================================')
    if usersel == '1':
        print('Loading... ...')
        time.sleep(2)
        Clear()
        if ((accbalance - 10) - 150) == 0 or ((accbalance - 10) - 150) <0:
            print('Insufficient amount.\nMinimum of RM 10 is required in your bank account.')
            UserOpt()
        else:
            print('Payment success!')
            accbalance = accbalance - 30
            print('Your new account balance\t: RM', accbalance)
            print('Transaction Date/Time: ',(dt.strftime("%x")),(dt.strftime("%X")))
            UserOpt()
    elif usersel == '2':
        print('Loading... ...')
        time.sleep(2)
        Clear()
        print('\t[1] Yes\n\t[2] No')
        usersel2 = input('Would you wish to continue to bills payment? (1/2)\t: ')
        print('===============================================================')
        if usersel2 == '1':
            print('Loading... ...')
            time.sleep(2)
            Bills()
        elif usersel2 == '2':
            UserOpt()
        else:
            print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
            print('Returning... ...')
            print('===============================================================')
            time.sleep(2)
            BillsOpt2()
    else:
        print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
        print('Returning... ...')
        print('===============================================================')
        time.sleep(2)
        BillsOpt2()
        
#Astro bill payment function
def BillsOpt3():
    global accbalance
    Clear()
    print('\t[1] Yes\n\t[2] No')
    usersel = input('Confirm payment RM 250? (1/2)\t: ')
    print('===============================================================')
    if usersel == '1':
        print('Loading... ...')
        time.sleep(2)
        Clear()
        if ((accbalance - 10) - 250) == 0 or ((accbalance - 10) - 250) <0:
            print('Insufficient amount.\nMinimum of RM 10 is required in your bank account.')
            UserOpt()
        else:
            print('Payment success!')
            accbalance = accbalance - 30
            print('Your new account balance\t: RM', accbalance)
            UserOpt()
    elif usersel == '2':
        print('Loading... ...')
        time.sleep(2)
        Clear()
        print('\t[1] Yes\n\t[2] No')
        usersel2 = input('Would you wish to continue to bills payment? (1/2)\t: ')
        print('===============================================================')
        if usersel2 == '1':
            print('Loading... ...')
            time.sleep(2)
            Bills()
        elif usersel2 == '2':
            UserOpt()
        else:
            print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
            print('Returning... ...')
            print('===============================================================')
            time.sleep(2)
            BillsOpt3()
    else:
        print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
        print('Returning... ...')
        print('===============================================================')
        time.sleep(2)
        BillsOpt3()

#Credit card bill payment function
def BillsOpt4():
    global accbalance
    Clear()
    print('\t[1] Yes\n\t[2] No')
    usersel = input('Confirm payment RM 3560? (1/2)\t: ')
    print('===============================================================')
    if usersel == '1':
        print('Loading... ...')
        time.sleep(2)
        Clear()
        if ((accbalance - 10) - 3560) == 0 or ((accbalance - 10) - 3560) <0:
            print('Insufficient amount.\nMinimum of RM 10 is required in your bank account.')
            UserOpt()
        else:
            print('Payment success!')
            accbalance = accbalance - 30
            print('Your new account balance\t: RM', accbalance)
            print('Transaction Date/Time: ',(dt.strftime("%x")),(dt.strftime("%X")))
            UserOpt()
    elif usersel == '2':
        print('Loading... ...')
        time.sleep(2)
        Clear()
        print('\t[1] Yes\n\t[2] No')
        usersel2 = input('Would you wish to continue to bills payment? (1/2)\t: ')
        print('===============================================================')
        if usersel2 == '1':
            print('Loading... ...')
            time.sleep(2)
            Bills()
        elif usersel2 == '2':
            UserOpt()
        else:
            print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
            print('Returning... ...')
            print('===============================================================')
            time.sleep(2)
            BillsOpt4()
    else:
        print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
        print('Returning... ...')
        print('===============================================================')
        time.sleep(2)
        BillsOpt4()

#Oversea money tansfer function
def Overseas():
    Clear()
    print('\t[1] Singapore\n\t[2] Taiwan\n\t[3] United States\n\t[4] Thailand\n\t[5] China')
    usersel = input('Please insert which country are you at (1-5)\t: ')
    print('===============================================================')
    if usersel == '1':
        print('Loading... ...')
        time.sleep(2)
        Sing()
    elif usersel == '2':
        print('Loading... ...')
        time.sleep(2)
        Taiwan()
    elif usersel == '3':
        print('Loading... ...')
        time.sleep(2)
        US()
    elif usersel == '4':
        print('Loading... ...')
        time.sleep(2)
        Thai()
    elif usersel == '5':
        print('Loading... ...')
        time.sleep(2)
        Chn()
    else:
        print('Request DENIED.\nPlease insert ONLY the option given. (1-5)')
        print('Returning... ...')
        print('===============================================================')
        time.sleep(2)
        Overseas()

#Transfer MYR to SGD function
def Sing():
    global accbalance
    Clear()
    usersel = float(input('How much SGD would you wish to withdraw\t: SGD = '))
    print('===============================================================')
    stat = round(usersel*3.08,2)
    print('Loading... ...')
    time.sleep(2)
    Clear()
    print(usersel,'SGD = RM',stat)
    print('\t[1] Yes\n\t[2] No')
    usersel2 = input('Confirm withdraw? (1/2)\t: ')
    print('===============================================================')
    if usersel2 == '1':
        print('Loading... ...')
        time.sleep(2)
        if ((accbalance - 10) - stat) == 0 or ((accbalance - 10) - stat) < 0:
            print('Insufficient amount.\nMinimum of RM 10 is required in your bank account')
            OverseasOpt()
        else:        
            accbalance = accbalance - stat
            print(usersel,'SGD had withdrawn successfully!')
            print('Your new account balance\t: RM', accbalance)
            print('Transaction Date/Time: ',(dt.strftime("%x")),(dt.strftime("%X")))
            print('===============================================================')
            UserOpt()
    elif usersel2 == '2':
        OverseasOpt()
    else:
        print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
        print('Returning... ...')
        print('===============================================================')
        time.sleep(2)
        OverseasOpt()

#Transfer MYR to TWD function    
def Taiwan():
    global accbalance
    Clear()
    usersel = float(input('How much TWD would you wish to withdraw\t: TWD = '))
    print('===============================================================')
    stat = round(usersel*0.15,2)
    print('Loading... ...')
    time.sleep(2)
    Clear()
    print(usersel,'TWD = RM',stat)
    print('\t[1] Yes\n\t[2] No')
    usersel2 = input('Confirm withdraw? (1/2)\t: ')
    print('===============================================================')
    if usersel2 == '1':
        print('Loading... ...')
        time.sleep(2)
        if ((accbalance - 10) - stat) == 0 or ((accbalance - 10) - stat) < 0:
            print('Insufficient amount.\nMinimum of RM 10 is required in your bank account')
            OverseasOpt()
        else:        
            accbalance = accbalance - stat
            print(usersel,'TWD had withdrawn successfully!')
            print('Your new account balance\t: RM', accbalance)
            print('Transaction Date/Time: ',(dt.strftime("%x")),(dt.strftime("%X")))
            print('===============================================================')
            UserOpt()
    elif usersel2 == '2':
        OverseasOpt()
    else:
        print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
        print('Returning... ...')
        print('===============================================================')
        time.sleep(2)
        OverseasOpt()

#Transfer MYR to USD function   
def US():
    global accbalance
    Clear()
    usersel = float(input('How much USD would you wish to withdraw\t: USD = '))
    print('===============================================================')
    stat = round(usersel*4.14,2)
    print('Loading... ...')
    time.sleep(2)
    Clear()
    print(usersel,'USD = RM',stat)
    print('\t[1] Yes\n\t[2] No')
    usersel2 = input('Confirm withdraw? (1/2)\t: ')
    print('===============================================================')
    if usersel2 == '1':
        print('Loading... ...')
        time.sleep(2)
        if ((accbalance - 10) - stat) == 0 or ((accbalance - 10) - stat) < 0:
            print('Insufficient amount.\nMinimum of RM 10 is required in your bank account')
            OverseasOpt()
        else:        
            accbalance = accbalance - stat
            print(usersel,'USD had withdrawn successfully!')
            print('Your new account balance\t: RM', accbalance)
            print('Transaction Date/Time: ',(dt.strftime("%x")),(dt.strftime("%X")))
            print('===============================================================')
            UserOpt()
    elif usersel2 == '2':
        OverseasOpt()
    else:
        print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
        print('Returning... ...')
        print('===============================================================')
        time.sleep(2)
        OverseasOpt()


#Transfer MYR to THB function
def Thai():
    global accbalance
    Clear()
    usersel = float(input('How much THB would you wish to withdraw\t: THB = '))
    print('===============================================================')
    stat = round(usersel*0.13,2)
    print('Loading... ...')
    time.sleep(2)
    Clear()
    print(usersel,'THB = RM',stat)
    print('\t[1] Yes\n\t[2] No')
    usersel2 = input('Confirm withdraw? (1/2)\t: ')
    print('===============================================================')
    if usersel2 == '1':
        print('Loading... ...')
        time.sleep(2)
        if ((accbalance - 10) - stat) == 0 or ((accbalance - 10) - stat) < 0:
            print('Insufficient amount.\nMinimum of RM 10 is required in your bank account')
            OverseasOpt()
        else:        
            accbalance = accbalance - stat
            print(usersel,'THB had withdrawn successfully!')
            print('Your new account balance\t: RM', accbalance)
            print('Transaction Date/Time: ',(dt.strftime("%x")),(dt.strftime("%X")))
            print('===============================================================')
            UserOpt()
    elif usersel2 == '2':
        OverseasOpt()
    else:
        print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
        print('Returning... ...')
        print('===============================================================')
        time.sleep(2)
        OverseasOpt()

#Transfer MYR to CNY function
def Chn():
    global accbalance
    Clear()
    usersel = float(input('How much CNY would you wish to withdraw\t: CNY = '))
    print('===============================================================')
    stat = round(usersel*0.63,2)
    print('Loading... ...')
    time.sleep(2)
    Clear()
    print(usersel,'CNY = RM',stat)
    print('\t[1] Yes\n\t[2] No')
    usersel2 = input('Confirm withdraw? (1/2)\t: ')
    print('===============================================================')
    if usersel2 == '1':
        print('Loading... ...')
        time.sleep(2)
        if ((accbalance - 10) - stat) == 0 or ((accbalance - 10) - stat) < 0:
            print('Insufficient amount.\nMinimum of RM 10 is required in your bank account')
            OverseasOpt()
        else:        
            accbalance = accbalance - stat
            print(usersel,'CNY had withdrawn successfully!')
            print('Your new account balance\t: RM', accbalance)
            print('Transaction Date/Time: ',(dt.strftime("%x")),(dt.strftime("%X")))
            print('===============================================================')
            UserOpt()
    elif usersel2 == '2':
        OverseasOpt()
    else:
        print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
        print('Returning... ...')
        print('===============================================================')
        time.sleep(2)
        OverseasOpt()

#Repeat oversea money tansfer or exit function
def OverseasOpt():
    Clear()
    print('Loading... ...')
    time.sleep(2)
    Clear()
    print('\t[1] Yes\n\t[2] No')
    usersel = input('Would you wish to go back to overseas usage? (1/2)\t: ')
    print('===============================================================')
    if usersel == '1':
        print('Loading... ...')
        time.sleep(2)
        Overseas()
    elif usersel == '2':
        UserOpt()
    else:
        print('Request DENIED.\nPlease insert ONLY the option given. (1/2)')
        print('Returning... ...')
        print('===============================================================')
        time.sleep(2)
        OverseasOpt()

#Close function
def Shutdown():
    Clear()
    print(thanks)
    print('Leaving... ...')
    print('===============================================================')
    time.sleep(2)
    exit()

######      Main Program      ######
startup()
