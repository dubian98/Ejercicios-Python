Algoritmo DPLL
Type Markdown and LaTeX: α2
Literales
Una literal es una variable proposicional afirmada o negada. La siguiente es una clase de Python que representa una literal. El constructor recibe el nombre de una variable como primer argumento y si esta es afirmada (positive = True) o negada (positive = False).

Las literales negadas se representan como precedidas por una tilde (~).

import re
class Literal:
    
    # regular expression for a valid variable name
    ID_REGEXP = re.compile(r"^[^\d\W]\w*\Z", re.UNICODE)
    
    """
    Propositional sentence tha is a variable or a negated variable
    """
    
    def __init__(self,variable,positive=True):
        """
        Creates the literal for the given variable
        :param variable: the variable of the literal
        :param positive: positive literal if True, negative literal if false
​
        """
        if re.match(Literal.ID_REGEXP,variable):
            self.variable = variable
        else:
            raise SyntaxError("Invalid variable name: '"+variable+"'")
        self.positive = positive
        
    @staticmethod
    def parse(s):
        s = s.replace(" ","")
        positive = not s.startswith("~")
        return Literal(s if positive else s[1:],positive)
​
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return ("" if self.positive else "~")+self.variable
        
    def __hash__(self):
        return hash(self.__str__())
    
    def __eq__(self,other):
        return self.__str__()==other.__str__()
    
    def __invert__(self):
        return Literal(self.variable,not self.positive)
l1 = Literal("A")
l2 = Literal("B",False)
l3 = Literal("C")
l4 = ~l3
print(l1,l2,l3,l4)
A ~B C ~C
Cláusulas
Una cláusula es una disyunción de literales. La siguiente es una clase en Python para representar una cláusula. El constructor recibe como primer argumento las literales que forman parte de la cláusula. Un segundo argumento del constructor indica cuando la representación de dichas literales es usando un conjunto que admite hashing.

class Clause:
    """
    A propositional clause
    This class keeps a singleton pattern of the clause with frozen hash
    so that any simplification can be propagated to sets and dictionaries
    in a single operation
    """
    
    def __init__(self, literals=None,frozen_hash=True):
        """
        cretates the clause with the provided set of literals
        :param literals: the set of literals
        :param frozen_hash: if true the hash is not based on content
        """
        self.frozen_hash = frozen_hash
        if literals:
            self.literals = frozenset(literals) if frozen_hash else literals
        else:
            self.literals = set()
        
    def __hash__(self):
        """
        the hash number is the memory location when the flag
        frozen_hash is True, otherwise the hash is the same as the 
        hash of the internal frozenset containing the literals
        :returns: the hash number of the clause
        """
        return id(self) if self.frozen_hash else hash(self.literals)
    
    def __eq__(self,other):
        """
        Equality between different instances of the same clause is only checked
        when frozen_hash is False. If frozen_hash is True, the method will
        return True, only for the same instance of the class
        """
        if self.__hash__()==hash(other):
            if self.frozen_hash:
                return True
            else:
                return self.literals == other.literals
        else:
            return False
    
    def __iadd__(self,literal):
        """
        adds the literal to the clause
        :param literal: the literal to add
        """
        if isinstance(literal,Literal):
            self.literals = self.literals.union({literal})
            return self
        else:
            raise TypeError("An argument of type Literal was expected")
            
    def __add__(self,literal):
        """
        adds the literal to the clause
        :param literal: the literal to add
        """
        if isinstance(literal,Literal):
            return Clause(self.literals.union({literal}),self.frozen_hash)
        else:
            raise TypeError("An argument of type Literal was expected")
            
    def __isub__(self,literal):
        """
        deletes a literal from the clause
        :param literal: the literal to substract
        """
        if isinstance(literal, Literal):
            self.literals = self.literals.difference({literal})
            return self
        else:
            raise TypeError("A literal of type string was expected")
​
    def __sub__(self,literal):
        """
        deletes a literal from the clause
        :param literal: the literal to substract
        """
        if isinstance(literal, Literal):
            return Clause(self.literals.difference({literal}),self.frozen_hash)
        else:
            raise TypeError("A literal of type string was expected")
        
    def __str__(self):
        return "( "+" | ".join(map(str,self.literals))+" )"
    
    def __repr__(self):
        return self.__str__()
    
    def __iter__(self):
        return (i for i in self.literals)
    
    def __len__(self):
        return len(self.literals)
    
    def copy(self):
        return Clause(self.literals.copy(),self.frozen_hash)
Ejemplo creamos una cláusula c1 formada por las literales l1 y l2
c1 = Clause({l1,l2})
print(c1)
( ~B | A )
Fórmula en Forma Normal Conjuntiva
Una formula en Forma Normal Conjuntiva (FNC) es una conjunción de literales.
Toda fórmula proposicional admite llevarse a su FNC.
​
A continuación te proporcionamos una clase para representar fórmulas en FNC.
En el constructor, el primer argumento recibe la fórmula en una cadena.
​
Para definir una fórmula:
El símbolo de la disyunción es una barra vertical (|).
El símbolo de la conjunción es el símbolo et (&).
import logging as log
class FormulaCNF:
    """
    Formula in Conjunctive Normal Form
    :param formula: CNF formula (string to parse)
    example: '(A|!B)&(!A|B|C)'
    """
    def __init__(self,formula=None,assignment=None):
        #removes all white spaces
        if formula:
            formula = ''.join(formula.split())
            (self.variables,self.clauses) = self.parse(formula)
            self.build_dicts()  
            if assignment:
                self.assignment = assignment.copy()
            else:
                self.assignment = set()
            
            if log.getLogger().isEnabledFor(log.DEBUG):
                log.debug(self.string_internals())
        else:
            self.clauses = set()
            self.assignment = set()
                
    def __getitem__(self,literal):
        """
        short notation for the simplify method
        :returns: the simplified formula resulting from assuming the literal
        is true
        """
        return self.simplify(literal)
            
    def empty_sentence(self):
        """
        :returns: true if the formula has no clauses
        """
        return not self.clauses
    
    def empty_clause(self):
        """
        :returns: true if there is an empty clause
        """
        return 0 in self.n_to_c
    
    def get_unit_clause_literal(self):
        """
        Gets a unit clause if there is one, None otherwise
        """
        clause = next(iter(self.n_to_c[1])) \
        if 1 in self.n_to_c else {}
        return next(iter(clause)) if clause else None
​
    def get_pure_literal(self):
        """
        Gest a pure literal
        """
        return next(iter(self.P)) if self.P else None
    
    def get_variable_literal(self):
        """
        Obtiene una variable de la formula
        """
        return Literal(next(iter(self.variables))) if self.variables else None
​
    def simplify(self,literal):
        """
        Simplifies the current sentence assming the provided literal
        :param literal: the literal to assume as true
        """
        log.debug("simplifying literal: "+str(literal))
        if not literal:
            raise ValueError(
                    "Invalid literal provided as argument: "+ str(literal))
        
        # stores the assignment
        self.assignment.add(literal)
        # deletes the variable of the literal
        self.variables = self.variables - {literal.variable}
        # updates the list of literals
        self.L = self.L -{literal}
        # updates the list of pure literals
        if self.isPureLiteral(literal):
            self.P = self.P - {literal}
        # deals with the clauses to delete
        if literal in self.l_to_c:
            for clause in self.l_to_c[literal].copy():
                self.remove_clause(clause)
                #TODO remover las cláusulas de otras entradas en l_to_c
                # update data structures for other literals
                for l in clause.copy():
                    self.decrease_literal_count(l)
                    self.del_from_dictionary_of_sets(
                            self.l_to_c,l,clause,True)
            #removes the entry from dicionary literal to clauses
            #del self.l_to_c[literal]
            
        # deals with the literals to delete negated literal
        neg_literal = ~literal 
        # updates list of literals
        self.L = self.L - {neg_literal}
        # deletes all negated literals from clauses
        if neg_literal in self.l_to_c:
            for clause in self.l_to_c[neg_literal]:
                self.remove_literal_from_clause(neg_literal,clause)
        # delete entry for negated literal from dictionary literal to clauses
        if neg_literal in self.l_to_c:
            del self.l_to_c[neg_literal]
        # updates list of negated literals
        if self.isPureLiteral(neg_literal):
            self.P = self.P - {neg_literal}
​
        log.debug("simplified formula:")
        if log.getLogger().isEnabledFor(log.DEBUG):
            log.debug(self.string_internals())
        return self
    
    def remove_clause(self,clause):
        """
        Removes the clause from data structures
        :parama clause: the clause to delete
        """
        # deletes clause from inverse map counts
        self.clauses.remove(clause)
        n = len(clause)
        self.del_from_dictionary_of_sets(self.n_to_c,n,clause,True)
    
    def remove_literal_from_clause(self,literal,clause):
        # frozen_hash allows for unique clause 
        # all clauses are updated (they are the same clause) 
        m = len(clause)
        # remove clause from map of counts to clauses
        self.del_from_dictionary_of_sets(self.n_to_c,m,clause,True)
        # obtain simplified clause
        clause -= literal
        # update map of count to clauses
        self.add_to_dictionary_of_sets(self.n_to_c,m-1,clause)
        # update other counts related to the literal
        self.decrease_literal_count(literal)
        
                
    def decrease_literal_count(self,literal):
        # decrease number to literal counts
        # delete literal from previous count
        n = self.l_to_n[literal]
        self.del_from_dictionary_of_sets(self.n_to_l,n,literal,True)
        # update the literal count if it is not zero
        self.add_to_dictionary_of_sets(self.n_to_l,n-1,literal)
        
        # update counts for the literal
        if literal in self.l_to_n:
            self.l_to_n[literal] -= 1
        else:
            raise ValueError("Inconsistent counts for literal: "+str(literal))
            
    def isPureLiteral(self,literal):
        """
        :returns: true if the literal is pure
        """
        return literal in self.P
    
        
    def parse(self,formula):
        """
        Parses the CNF formula string
        """
        variables = set()
        clauses = set()
        clstr = re.findall("[^&]+",formula)
        for c in clstr:
            literals = re.findall("[^\(\)\|]+",c)
            clause = Clause()
            for l in literals:
                literal = Literal.parse(l)
                variables.add(literal.variable)
                clause += literal
            clauses.add(clause)
        return (variables,clauses)
    
    
    def build_dicts(self):
        """
        Builds dictionaries for efficient access
        to clauses and literals
        l_to_c: dictionary, keys are literals, values are clauses
        n_to_c: dictionary, keys are sizes, values are clauses
        l_to_n: dictionary, keys are literals, values are counts
        n_to_c: dictionary, keys are counts, values are clauses
        L: set, all literals in the formula
        P: set, all pure literals in the formula
        """
        # W gives fast access to clauses by literals
        self.l_to_c = {}
        # n gives fast access to clauses by size
        self.n_to_c = {}
        # literal to counts
        self.l_to_n = {}
        # counts to literals
        self.n_to_l = {}
        
        for c in self.clauses:
            # build dictionary indexed by size
            self.add_to_dictionary_of_sets(self.n_to_c,len(c),c)
            for l in c:
                #builds dictionary indexed by literal
                self.add_to_dictionary_of_sets(self.l_to_c,l,c)
                #compute frecuency of literals
                self.l_to_n[l] = self.l_to_n[l] + 1 if l in self.l_to_n else 1
                
        #reverse literal counts
        self.L = set()
        for k,v in self.l_to_n.items():
            self.add_to_dictionary_of_sets(self.n_to_l,v,k)
            self.L.add(k)
        self.P = {v for v in self.L if ~v not in self.L}
    
    def add_to_dictionary_of_sets(self,d,k,v):
        """
        Adds a value to a dictionary of sets
        :param d: the dictionary
        :param k: the key
        :param v: the value to add
        :param by_len: True if the key is the length of the set to add
        """
        singleton = {v}
        d[k] = d[k].union(singleton) if k in d else singleton
        
    def del_from_dictionary_of_sets(self,d,k,m,del_key):
        """
        Deletes a set member from a dictionary of sets
        :param d: the dictionary
        :param k: the key
        :parma m: the member of the set to delete
        :del_key: if this flag is True the entry is removed when set is empty
        """
        # removes with set difference
        d[k] = d[k] - {m}
        if del_key and not d[k]:
            del d[k]
    
    def copy(self):
        """
        Creates a shallow copy of the CNF formula
        """
        log.debug("Creating a copy of the current CNF formula")
        formula = FormulaCNF(str(self),self.assignment)
        return formula
    
    def string_internals(self):
        return ("clauses:"+str(self.clauses)+"\n"+
        "variables:"+str(self.variables)+"\n"+
        "assignment:"+str(self.assignment)+"\n"+
        "l_to_c:"+str(self.l_to_c)+"\n"+
        "n_to_c:"+str(self.n_to_c)+"\n"+
        "l_to_n:"+str(self.l_to_n)+"\n"+
        "n_to_l:"+str(self.n_to_l)+"\n"+
        "L:"+str(self.L)+"\n"+
        "P:"+str(self.P))
    
    def __str__(self):
        return " & ".join(map(str,self.clauses))
    
    def __repr__(self):
        return self.__str__()
phi = FormulaCNF("(A|~B)&(~A|C)&(~B|~C)&(C)")
print(phi)
( ~B | A ) & ( ~A | C ) & ( ~B | ~C ) & ( C )
phi.empty_sentence()
False
phi.empty_clause()
False
#De existir una clúsula unitaria, obtiene la literal de la cláusula. Regresa None si no existe
l = phi.get_unit_clause_literal()
print(l)
C
#Obtiene una literal pura de existir, None si no existe
l = phi.get_pure_literal()
print(l)
~B
#Obtiene una literal con una variable arbitraria de la formula phi
v = phi.get_variable_literal()
print(v)
A
#Obtiene una copia de la formula
psi = phi.copy()
print(psi)
( ~B | A ) & ( C ) & ( ~A | C ) & ( ~B | ~C )
psi = phi[l]
print(psi)
( ~A | C ) & ( C )
a = phi.assignment
print(a)
{~B}
class DPLL:
    """
    DPLL algorithm
    """
    @staticmethod
    def satisfiable(phi,reporter=None):
        """
        determines if phi is satisfiable
        :param phi: a CNF formula
        """
        if phi.empty_sentence():
            return (True,phi.assignment)
        else:
            return(False,None)
phi_1 = FormulaCNF("(~x1 | x3 | x4) & (~x2 | x6 | x4) & (~x2 | ~x6 | ~x3) & (~x4 | ~x2) & (x2 | ~x3 | ~x1) & (x2 | x6 | x3) & (x2 | ~x6 | ~x4) & (x1 | x5) & (x1 | x6) & (~x6 | x3 | ~x5) & (x1 | ~x3 | ~x5)")
DPLL.satisfiable(phi_1)
(False, None)