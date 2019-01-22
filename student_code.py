import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
        print("Asserting {!r}".format(fact))

        if isinstance(fact, Fact):
            add = False

            if len(self.facts) == 0:
                self.facts.append(fact)
            else:
                for f in self.facts:                   
                    if f == fact:
                        add = False
                        break
                    else:
                        add = True
            
            if add:
                self.facts.append(fact)

            
            
                
        
    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        
        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """
        

        print("Asking {!r}".format(fact))

        blst = ListOfBindings()

        if isinstance(fact,Fact):
            for f in self.facts:
                bdigs = match(fact.statement,f.statement)
                if bdigs != False:
                    blst.add_bindings(bdigs,[f])

                

        if (len(blst.list_of_bindings) != 0):
            return blst
        else:
            return False    
        




