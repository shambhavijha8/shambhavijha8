{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Function to deposite amount\n",
    "def deposit(self):\n",
    "\t\tamount = float(input(\"Enter amount to be deposited: \"))\n",
    "\t\tself.balance += amount\n",
    "\t\tprint(\"\\n Amount Deposited:\", amount)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Function to withdraw the amount\n",
    "def withdraw(self):\n",
    "\t\tamount = float(input(\"Enter amount to be withdrawn: \"))\n",
    "\t\tif self.balance >= amount:\n",
    "\t\t\tself.balance -= amount\n",
    "\t\t\tprint(\"\\n You Withdrew:\", amount)\n",
    "\t\telse:\n",
    "\t\t\tprint(\"\\n Insufficient balance \")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Function to display the amount\n",
    "def display(self):\n",
    "\t\tprint(\"\\n Net Available Balance =\", self.balance)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello!!! Welcome to the Deposit & Withdrawal Machine\n",
      "Enter amount to be Deposited: 3000\n",
      "\n",
      " Amount Deposited: 3000.0\n"
     ]
    }
   ],
   "source": [
    "# Python program to create Bankaccount class\n",
    "# with both a deposit() and a withdraw() function\n",
    "class Bank_Account:\n",
    "\tdef __init__(self):\n",
    "\t\tself.balance=0\n",
    "\t\tprint(\"Hello!!! Welcome to the Deposit & Withdrawal Machine\")\n",
    "\n",
    "\tdef deposit(self):\n",
    "\t\tamount=float(input(\"Enter amount to be Deposited: \"))\n",
    "\t\tself.balance += amount\n",
    "\t\tprint(\"\\n Amount Deposited:\",amount)\n",
    "\n",
    "\tdef withdraw(self):\n",
    "\t\tamount = float(input(\"Enter amount to be Withdrawn: \"))\n",
    "\t\tif self.balance>=amount:\n",
    "\t\t\tself.balance-=amount\n",
    "\t\t\tprint(\"\\n You Withdrew:\", amount)\n",
    "\t\telse:\n",
    "\t\t\tprint(\"\\n Insufficient balance \")\n",
    "\n",
    "\tdef display(self):\n",
    "\t\tprint(\"\\n Net Available Balance=\",self.balance)\n",
    "\n",
    "# Driver code\n",
    "\n",
    "# creating an object of class\n",
    "s = Bank_Account()\n",
    "\n",
    "# Calling functions with that class object\n",
    "s.deposit()\n",
    "s.withdraw()\n",
    "s.display()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
