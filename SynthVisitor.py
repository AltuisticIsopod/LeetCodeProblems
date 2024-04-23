# Generated from Synth.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SynthParser import SynthParser
else:
    from SynthParser import SynthParser

# This class defines a complete generic visitor for a parse tree produced by SynthParser.

class SynthVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SynthParser#program.
    def visitProgram(self, ctx:SynthParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynthParser#block.
    def visitBlock(self, ctx:SynthParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynthParser#function.
    def visitFunction(self, ctx:SynthParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynthParser#declaration.
    def visitDeclaration(self, ctx:SynthParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynthParser#command.
    def visitCommand(self, ctx:SynthParser.CommandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynthParser#incrementOperation.
    def visitIncrementOperation(self, ctx:SynthParser.IncrementOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynthParser#ternary.
    def visitTernary(self, ctx:SynthParser.TernaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynthParser#booleanExpr.
    def visitBooleanExpr(self, ctx:SynthParser.BooleanExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynthParser#expression.
    def visitExpression(self, ctx:SynthParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynthParser#additionExpr.
    def visitAdditionExpr(self, ctx:SynthParser.AdditionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynthParser#multiplicativeExpr.
    def visitMultiplicativeExpr(self, ctx:SynthParser.MultiplicativeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynthParser#unaryExpr.
    def visitUnaryExpr(self, ctx:SynthParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynthParser#stringExpr.
    def visitStringExpr(self, ctx:SynthParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynthParser#functionCall.
    def visitFunctionCall(self, ctx:SynthParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynthParser#parameters.
    def visitParameters(self, ctx:SynthParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynthParser#params.
    def visitParams(self, ctx:SynthParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SynthParser#number.
    def visitNumber(self, ctx:SynthParser.NumberContext):
        return self.visitChildren(ctx)



del SynthParser