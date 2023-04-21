; ModuleID = 'teste.ll'
source_filename = "teste.c"
target datalayout = "e-m:e-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@.str = private unnamed_addr constant [45 x i8] c"Insira o numero de linhas que a matriz tera\0A\00", align 1
@.str.1 = private unnamed_addr constant [3 x i8] c"%d\00", align 1
@.str.2 = private unnamed_addr constant [46 x i8] c"Insira o numero de colunas que a matriz tera\0A\00", align 1
@.str.3 = private unnamed_addr constant [30 x i8] c"Insira a posicao i=%d e j=%d\0A\00", align 1
@.str.4 = private unnamed_addr constant [4 x i8] c"%d\09\00", align 1
@.str.5 = private unnamed_addr constant [2 x i8] c"\0A\00", align 1
@.str.6 = private unnamed_addr constant [62 x i8] c"Insira o ponto que voce quer calcular a media dos adjacentes\0A\00", align 1
@.str.7 = private unnamed_addr constant [9 x i8] c"\0ALinha: \00", align 1
@.str.8 = private unnamed_addr constant [10 x i8] c"\0AColuna: \00", align 1
@.str.9 = private unnamed_addr constant [58 x i8] c"A media dos pontos adjacentes do ponto escolhido e: %.3f\0A\00", align 1

; Function Attrs: noinline nounwind uwtable
define i32 @main() #0 {
  %1 = alloca i32, align 4
  %2 = alloca i32, align 4
  %3 = alloca i32, align 4
  %4 = alloca i32, align 4
  %5 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([45 x i8], [45 x i8]* @.str, i32 0, i32 0))
  %6 = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.1, i32 0, i32 0), i32* %1)
  %7 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([46 x i8], [46 x i8]* @.str.2, i32 0, i32 0))
  %8 = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.1, i32 0, i32 0), i32* %2)
  %9 = load i32, i32* %1, align 4
  %10 = zext i32 %9 to i64
  %11 = load i32, i32* %2, align 4
  %12 = zext i32 %11 to i64
  %13 = call i8* @llvm.stacksave()
  %14 = mul nuw i64 %10, %12
  %15 = alloca i32, i64 %14, align 16
  store i32 0, i32* %3, align 4
  br label %16

16:                                               ; preds = %43, %0
  %17 = load i32, i32* %3, align 4
  %18 = load i32, i32* %1, align 4
  %19 = icmp slt i32 %17, %18
  br i1 %19, label %20, label %46

20:                                               ; preds = %16
  store i32 0, i32* %4, align 4
  br label %21

21:                                               ; preds = %39, %20
  %22 = load i32, i32* %4, align 4
  %23 = load i32, i32* %2, align 4
  %24 = icmp slt i32 %22, %23
  br i1 %24, label %25, label %42

25:                                               ; preds = %21
  %26 = load i32, i32* %3, align 4
  %27 = add nsw i32 %26, 1
  %28 = load i32, i32* %4, align 4
  %29 = add nsw i32 %28, 1
  %30 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([30 x i8], [30 x i8]* @.str.3, i32 0, i32 0), i32 %27, i32 %29)
  %31 = load i32, i32* %3, align 4
  %32 = sext i32 %31 to i64
  %33 = mul nsw i64 %32, %12
  %34 = getelementptr inbounds i32, i32* %15, i64 %33
  %35 = load i32, i32* %4, align 4
  %36 = sext i32 %35 to i64
  %37 = getelementptr inbounds i32, i32* %34, i64 %36
  %38 = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.1, i32 0, i32 0), i32* %37)
  br label %39

39:                                               ; preds = %25
  %40 = load i32, i32* %4, align 4
  %41 = add nsw i32 %40, 1
  store i32 %41, i32* %4, align 4
  br label %21

42:                                               ; preds = %21
  br label %43

43:                                               ; preds = %42
  %44 = load i32, i32* %3, align 4
  %45 = add nsw i32 %44, 1
  store i32 %45, i32* %3, align 4
  br label %16

46:                                               ; preds = %16
  store i32 0, i32* %3, align 4
  br label %47

47:                                               ; preds = %71, %46
  %48 = load i32, i32* %3, align 4
  %49 = load i32, i32* %1, align 4
  %50 = icmp slt i32 %48, %49
  br i1 %50, label %51, label %74

51:                                               ; preds = %47
  store i32 0, i32* %4, align 4
  br label %52

52:                                               ; preds = %66, %51
  %53 = load i32, i32* %4, align 4
  %54 = load i32, i32* %2, align 4
  %55 = icmp slt i32 %53, %54
  br i1 %55, label %56, label %69

56:                                               ; preds = %52
  %57 = load i32, i32* %3, align 4
  %58 = sext i32 %57 to i64
  %59 = mul nsw i64 %58, %12
  %60 = getelementptr inbounds i32, i32* %15, i64 %59
  %61 = load i32, i32* %4, align 4
  %62 = sext i32 %61 to i64
  %63 = getelementptr inbounds i32, i32* %60, i64 %62
  %64 = load i32, i32* %63, align 4
  %65 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str.4, i32 0, i32 0), i32 %64)
  br label %66

66:                                               ; preds = %56
  %67 = load i32, i32* %4, align 4
  %68 = add nsw i32 %67, 1
  store i32 %68, i32* %4, align 4
  br label %52

69:                                               ; preds = %52
  %70 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([2 x i8], [2 x i8]* @.str.5, i32 0, i32 0))
  br label %71

71:                                               ; preds = %69
  %72 = load i32, i32* %3, align 4
  %73 = add nsw i32 %72, 1
  store i32 %73, i32* %3, align 4
  br label %47

74:                                               ; preds = %47
  %75 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([62 x i8], [62 x i8]* @.str.6, i32 0, i32 0))
  %76 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([9 x i8], [9 x i8]* @.str.7, i32 0, i32 0))
  %77 = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.1, i32 0, i32 0), i32* %3)
  %78 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([10 x i8], [10 x i8]* @.str.8, i32 0, i32 0))
  %79 = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @.str.1, i32 0, i32 0), i32* %4)
  %80 = load i32, i32* %3, align 4
  %81 = add nsw i32 %80, -1
  store i32 %81, i32* %3, align 4
  %82 = load i32, i32* %4, align 4
  %83 = add nsw i32 %82, -1
  store i32 %83, i32* %4, align 4
  %84 = load i32, i32* %3, align 4
  %85 = sub nsw i32 %84, 1
  %86 = icmp slt i32 %85, 0
  br i1 %86, label %87, label %88

87:                                               ; preds = %74
  br label %88

88:                                               ; preds = %87, %74
  %.01 = phi i32 [ 0, %87 ], [ 1, %74 ]
  %89 = load i32, i32* %3, align 4
  %90 = add nsw i32 %89, 1
  %91 = load i32, i32* %1, align 4
  %92 = sub nsw i32 %91, 1
  %93 = icmp sgt i32 %90, %92
  br i1 %93, label %94, label %95

94:                                               ; preds = %88
  br label %95

95:                                               ; preds = %94, %88
  %.0 = phi i32 [ 0, %94 ], [ 1, %88 ]
  %96 = load i32, i32* %4, align 4
  %97 = sub nsw i32 %96, 1
  %98 = icmp slt i32 %97, 0
  br i1 %98, label %99, label %100

99:                                               ; preds = %95
  br label %100

100:                                              ; preds = %99, %95
  %.03 = phi i32 [ 0, %99 ], [ 1, %95 ]
  %101 = load i32, i32* %4, align 4
  %102 = add nsw i32 %101, 1
  %103 = load i32, i32* %2, align 4
  %104 = sub nsw i32 %103, 1
  %105 = icmp sgt i32 %102, %104
  br i1 %105, label %106, label %107

106:                                              ; preds = %100
  br label %107

107:                                              ; preds = %106, %100
  %.02 = phi i32 [ 0, %106 ], [ 1, %100 ]
  %108 = load i32, i32* %3, align 4
  %109 = sext i32 %108 to i64
  %110 = mul nsw i64 %109, %12
  %111 = getelementptr inbounds i32, i32* %15, i64 %110
  %112 = load i32, i32* %4, align 4
  %113 = sext i32 %112 to i64
  %114 = getelementptr inbounds i32, i32* %111, i64 %113
  %115 = load i32, i32* %114, align 4
  %116 = sitofp i32 %115 to float
  %117 = fadd float 0.000000e+00, %116
  %118 = icmp eq i32 %.01, 1
  br i1 %118, label %119, label %132

119:                                              ; preds = %107
  %120 = load i32, i32* %3, align 4
  %121 = sub nsw i32 %120, 1
  %122 = sext i32 %121 to i64
  %123 = mul nsw i64 %122, %12
  %124 = getelementptr inbounds i32, i32* %15, i64 %123
  %125 = load i32, i32* %4, align 4
  %126 = sext i32 %125 to i64
  %127 = getelementptr inbounds i32, i32* %124, i64 %126
  %128 = load i32, i32* %127, align 4
  %129 = sitofp i32 %128 to float
  %130 = fadd float %117, %129
  %131 = add nsw i32 1, 1
  br label %132

132:                                              ; preds = %119, %107
  %.05 = phi float [ %130, %119 ], [ %117, %107 ]
  %.04 = phi i32 [ %131, %119 ], [ 1, %107 ]
  %133 = icmp eq i32 %.0, 1
  br i1 %133, label %134, label %147

134:                                              ; preds = %132
  %135 = load i32, i32* %3, align 4
  %136 = add nsw i32 %135, 1
  %137 = sext i32 %136 to i64
  %138 = mul nsw i64 %137, %12
  %139 = getelementptr inbounds i32, i32* %15, i64 %138
  %140 = load i32, i32* %4, align 4
  %141 = sext i32 %140 to i64
  %142 = getelementptr inbounds i32, i32* %139, i64 %141
  %143 = load i32, i32* %142, align 4
  %144 = sitofp i32 %143 to float
  %145 = fadd float %.05, %144
  %146 = add nsw i32 %.04, 1
  br label %147

147:                                              ; preds = %134, %132
  %.16 = phi float [ %145, %134 ], [ %.05, %132 ]
  %.1 = phi i32 [ %146, %134 ], [ %.04, %132 ]
  %148 = icmp eq i32 %.03, 1
  br i1 %148, label %149, label %162

149:                                              ; preds = %147
  %150 = load i32, i32* %3, align 4
  %151 = sext i32 %150 to i64
  %152 = mul nsw i64 %151, %12
  %153 = getelementptr inbounds i32, i32* %15, i64 %152
  %154 = load i32, i32* %4, align 4
  %155 = sub nsw i32 %154, 1
  %156 = sext i32 %155 to i64
  %157 = getelementptr inbounds i32, i32* %153, i64 %156
  %158 = load i32, i32* %157, align 4
  %159 = sitofp i32 %158 to float
  %160 = fadd float %.16, %159
  %161 = add nsw i32 %.1, 1
  br label %162

162:                                              ; preds = %149, %147
  %.27 = phi float [ %160, %149 ], [ %.16, %147 ]
  %.2 = phi i32 [ %161, %149 ], [ %.1, %147 ]
  %163 = icmp eq i32 %.02, 1
  br i1 %163, label %164, label %177

164:                                              ; preds = %162
  %165 = load i32, i32* %3, align 4
  %166 = sext i32 %165 to i64
  %167 = mul nsw i64 %166, %12
  %168 = getelementptr inbounds i32, i32* %15, i64 %167
  %169 = load i32, i32* %4, align 4
  %170 = add nsw i32 %169, 1
  %171 = sext i32 %170 to i64
  %172 = getelementptr inbounds i32, i32* %168, i64 %171
  %173 = load i32, i32* %172, align 4
  %174 = sitofp i32 %173 to float
  %175 = fadd float %.27, %174
  %176 = add nsw i32 %.2, 1
  br label %177

177:                                              ; preds = %164, %162
  %.38 = phi float [ %175, %164 ], [ %.27, %162 ]
  %.3 = phi i32 [ %176, %164 ], [ %.2, %162 ]
  %178 = sitofp i32 %.3 to float
  %179 = fdiv float %.38, %178
  %180 = fpext float %179 to double
  %181 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([58 x i8], [58 x i8]* @.str.9, i32 0, i32 0), double %180)
  call void @llvm.stackrestore(i8* %13)
  ret i32 0
}

declare i32 @printf(i8*, ...) #1

declare i32 @__isoc99_scanf(i8*, ...) #1

; Function Attrs: nocallback nofree nosync nounwind willreturn
declare i8* @llvm.stacksave() #2

; Function Attrs: nocallback nofree nosync nounwind willreturn
declare void @llvm.stackrestore(i8*) #2

attributes #0 = { noinline nounwind uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #2 = { nocallback nofree nosync nounwind willreturn }

!llvm.module.flags = !{!0}
!llvm.ident = !{!1}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{!"clang version 6.0.0-1ubuntu2 (tags/RELEASE_600/final)"}