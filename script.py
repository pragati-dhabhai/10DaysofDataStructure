{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# TASK 1ST"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "44"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "class Node:\n",
    "    def __init__(self,value,next_node=None):\n",
    "        self.value=value\n",
    "        self.next_node=next_node\n",
    "    def get_value(self):\n",
    "        return self.value\n",
    "    def get_next_node(self):\n",
    "        return self.next_node\n",
    "    def set_next_node(self,next_node):\n",
    "        self.next_node=next_node\n",
    "my_node=Node(44)\n",
    "my_node.get_value()        \n",
    "        "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# TASK 2nd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Node:\n",
    "    def __init__(self,value,next_node=None):\n",
    "        self.value=value\n",
    "        self.next_node=next_node\n",
    "    def get_value(self):\n",
    "        return self.value\n",
    "    def get_next_node(self):\n",
    "        return self.next_node\n",
    "    def set_next_node(self,next_node):\n",
    "        self.next_node=next_node\n",
    "my_node=Node(44)\n",
    "my_node.get_value()\n",
    "class LinkedList:\n",
    "    def __init__(self,value=None):\n",
    "        self.head_node=new_node(value)\n",
    "    def get_head_node(self):\n",
    "        return self.head_node"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# TASK 3rd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A\n"
     ]
    }
   ],
   "source": [
    "class Node:\n",
    "    def __init__(self,value,next_node=None):\n",
    "        self.value=value\n",
    "        self.next_node=next_node\n",
    "    def get_value(self):\n",
    "        return self.value\n",
    "    def get_next_node(self):\n",
    "        return self.next_node\n",
    "    def set_next_node(self,next_node):\n",
    "        self.next_node=next_node\n",
    "my_node=Node(44)\n",
    "my_node.get_value()\n",
    "class LinkedList:\n",
    "    def __init__(self,value=None):\n",
    "        self.head_node=value\n",
    "    def get_head_node(self):\n",
    "        return self.head_node \n",
    "    def insert_beginning(self,new_value):\n",
    "        new_node=Node(new_value)\n",
    "        self.head_node=new_node\n",
    "        new_node.next=self.head_node\n",
    "    def stringify_list(self):\n",
    "        node=self.head_node\n",
    "        while node:\n",
    "            print(str(node.value))\n",
    "            node=node.next_node\n",
    "l=LinkedList()\n",
    "l.insert_beginning('A')\n",
    "l.stringify_list()            \n",
    "        \n",
    "        "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# TASK 4th"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A\n"
     ]
    }
   ],
   "source": [
    "class Node:\n",
    "    def __init__(self,value,next_node=None):\n",
    "        self.value=value\n",
    "        self.next_node=next_node\n",
    "    def get_value(self):\n",
    "        return self.value\n",
    "    def get_next_node(self):\n",
    "        return self.next_node\n",
    "    def set_next_node(self,next_node):\n",
    "        self.next_node=next_node\n",
    "my_node=Node(44)\n",
    "my_node.get_value()\n",
    "class LinkedList:\n",
    "    def __init__(self,value=None):\n",
    "        self.head_node=value\n",
    "    def get_head_node(self):\n",
    "        return self.head_node \n",
    "    def insert_beginning(self,new_value):\n",
    "        new_node=Node(new_value)\n",
    "        self.head_node=new_node\n",
    "        new_node.next=self.head_node\n",
    "    def stringify_list(self):\n",
    "        node=self.head_node\n",
    "        while node:\n",
    "            print(str(node.value))\n",
    "            node=node.next_node\n",
    "    def remove_node(self,value_to_remove):\n",
    "        current_node=self.head_node\n",
    "        if self.head_node.value==value_to_remove:\n",
    "            self.head_node=current_node.next\n",
    "        else:   \n",
    "            while current_node.get_next_node().get_value()==current_node.get_next_node().get_value():\n",
    "                    current_node=next_node.get_next_node()\n",
    "        current_node=None            \n",
    "l=LinkedList()\n",
    "l.insert_beginning('A')\n",
    "l.stringify_list()         \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# TASK FINAL"
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
      "A\n",
      "B\n",
      "B\n",
      "B\n"
     ]
    }
   ],
   "source": [
    "class Node:\n",
    "    def __init__(self,value,next_node=None):\n",
    "        self.value=value\n",
    "        self.next_node=next_node\n",
    "    def get_value(self):\n",
    "        return self.value\n",
    "    def get_next_node(self):\n",
    "        return self.next_node\n",
    "    def set_next_node(self,next_node):\n",
    "        self.next_node=next_node\n",
    "my_node=Node(44)\n",
    "my_node.get_value()\n",
    "class LinkedList:\n",
    "    def __init__(self,value=None):\n",
    "        self.head_node=value\n",
    "    def get_head_node(self):\n",
    "        return self.head_node \n",
    "    def insert_beginning(self,new_value):\n",
    "        new_node=Node(new_value)\n",
    "        self.head_node=new_node\n",
    "        new_node.next=self.head_node\n",
    "    def stringify_list(self):\n",
    "        node=self.head_node\n",
    "        while node:\n",
    "            print(str(node.value))\n",
    "            node=node.next_node\n",
    "    def remove_node(self,value_to_remove):\n",
    "        current_node=self.head_node\n",
    "        if current_node.value==value_to_remove:\n",
    "            self.head_node=current_node.next\n",
    "        else:\n",
    "            print(current_node.value)\n",
    "            previous_node=None   \n",
    "            while current_node.value!=value_to_remove and current_node:\n",
    "                previous_node=current_node\n",
    "            if current_node is None:\n",
    "                return\n",
    "            previous_node.next_node=current_node.next_node\n",
    "        current_node=None            \n",
    "l=LinkedList()\n",
    "l.insert_beginning('A') \n",
    "l.stringify_list()\n",
    "l.insert_beginning('B')\n",
    "l.stringify_list()\n",
    "l.remove_node('A')\n",
    "l.stringify_list()\n",
    "l.remove_node('B')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
