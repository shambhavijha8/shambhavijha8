{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Yes\n"
     ]
    }
   ],
   "source": [
    "# Python 3 implementation of the approach\n",
    "\n",
    "# Function to check whether\n",
    "# it is possible to create a\n",
    "# polygon with given sides length\n",
    "def isPossible(a, n):\n",
    "\t# Sum stores the sum of all the sides\n",
    "\t# and maxS stores the length of\n",
    "\t# the largest side\n",
    "\tsum = 0\n",
    "\tmaxS = 0\n",
    "\tfor i in range(n):\n",
    "\t\tsum += a[i]\n",
    "\t\tmaxS = max(a[i], maxS)\n",
    "\n",
    "\t# If the length of the largest side\n",
    "\t# is less than the sum of the\n",
    "\t# other remaining sides\n",
    "\tif ((sum - maxS) > maxS):\n",
    "\t\treturn True\n",
    "\t\n",
    "\treturn False\n",
    "\n",
    "# Driver code\n",
    "a =[2, 3, 4]\n",
    "n = len(a)\n",
    "\n",
    "if(isPossible(a, n)):\n",
    "\tprint(\"Yes\")\n",
    "else:\n",
    "\tprint(\"No\")\n"
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
