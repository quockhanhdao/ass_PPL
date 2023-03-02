# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decllist.
    def visitDecllist(self, ctx:MT22Parser.DecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decllistprime.
    def visitDecllistprime(self, ctx:MT22Parser.DecllistprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decl.
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl.
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#initialization.
    def visitInitialization(self, ctx:MT22Parser.InitializationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramdecl.
    def visitParamdecl(self, ctx:MT22Parser.ParamdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcdecl.
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#prototype.
    def visitPrototype(self, ctx:MT22Parser.PrototypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement.
    def visitStatement(self, ctx:MT22Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assignstmt.
    def visitAssignstmt(self, ctx:MT22Parser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#ifstmt.
    def visitIfstmt(self, ctx:MT22Parser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#forstmt.
    def visitForstmt(self, ctx:MT22Parser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#whilestmt.
    def visitWhilestmt(self, ctx:MT22Parser.WhilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dowhilestmt.
    def visitDowhilestmt(self, ctx:MT22Parser.DowhilestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#breakstmt.
    def visitBreakstmt(self, ctx:MT22Parser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continuestmt.
    def visitContinuestmt(self, ctx:MT22Parser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#returnstmt.
    def visitReturnstmt(self, ctx:MT22Parser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#callstmt.
    def visitCallstmt(self, ctx:MT22Parser.CallstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#blockstmt.
    def visitBlockstmt(self, ctx:MT22Parser.BlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#scalar.
    def visitScalar(self, ctx:MT22Parser.ScalarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#specfunc.
    def visitSpecfunc(self, ctx:MT22Parser.SpecfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readInteger.
    def visitReadInteger(self, ctx:MT22Parser.ReadIntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printInteger.
    def visitPrintInteger(self, ctx:MT22Parser.PrintIntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readFloat.
    def visitReadFloat(self, ctx:MT22Parser.ReadFloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#writeFloat.
    def visitWriteFloat(self, ctx:MT22Parser.WriteFloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readBoolean.
    def visitReadBoolean(self, ctx:MT22Parser.ReadBooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printBoolean.
    def visitPrintBoolean(self, ctx:MT22Parser.PrintBooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readString.
    def visitReadString(self, ctx:MT22Parser.ReadStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printString.
    def visitPrintString(self, ctx:MT22Parser.PrintStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#sper.
    def visitSper(self, ctx:MT22Parser.SperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#preventDefault.
    def visitPreventDefault(self, ctx:MT22Parser.PreventDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression.
    def visitExpression(self, ctx:MT22Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#term1.
    def visitTerm1(self, ctx:MT22Parser.Term1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#term2.
    def visitTerm2(self, ctx:MT22Parser.Term2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#term3.
    def visitTerm3(self, ctx:MT22Parser.Term3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#term4.
    def visitTerm4(self, ctx:MT22Parser.Term4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#term5.
    def visitTerm5(self, ctx:MT22Parser.Term5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#subexpression.
    def visitSubexpression(self, ctx:MT22Parser.SubexpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idxop.
    def visitIdxop(self, ctx:MT22Parser.IdxopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call.
    def visitCall(self, ctx:MT22Parser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrlit.
    def visitArrlit(self, ctx:MT22Parser.ArrlitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#intlist.
    def visitIntlist(self, ctx:MT22Parser.IntlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idlist.
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expressionlist.
    def visitExpressionlist(self, ctx:MT22Parser.ExpressionlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramlist.
    def visitParamlist(self, ctx:MT22Parser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramlistprime.
    def visitParamlistprime(self, ctx:MT22Parser.ParamlistprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arglist.
    def visitArglist(self, ctx:MT22Parser.ArglistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arglistprime.
    def visitArglistprime(self, ctx:MT22Parser.ArglistprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#linelist.
    def visitLinelist(self, ctx:MT22Parser.LinelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#linelistprime.
    def visitLinelistprime(self, ctx:MT22Parser.LinelistprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#line.
    def visitLine(self, ctx:MT22Parser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#atomtyp.
    def visitAtomtyp(self, ctx:MT22Parser.AtomtypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrtyp.
    def visitArrtyp(self, ctx:MT22Parser.ArrtypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#voidtyp.
    def visitVoidtyp(self, ctx:MT22Parser.VoidtypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#autotyp.
    def visitAutotyp(self, ctx:MT22Parser.AutotypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#typ.
    def visitTyp(self, ctx:MT22Parser.TypContext):
        return self.visitChildren(ctx)



del MT22Parser