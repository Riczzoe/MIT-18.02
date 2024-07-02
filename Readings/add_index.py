from PyPDF2 import PdfReader, PdfWriter

def add_hierarchical_bookmarks(input_pdf, output_pdf):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # 复制页面
    for page in reader.pages:
        writer.add_page(page)

    contents = writer.add_bookmark('Contents', 6) 
    chapter10 = writer.add_bookmark('Chapter 10: Polar Coordinates And Plane Curves', 567-543)
    chapter11 = writer.add_bookmark('Chapter 11: Infinite Series', 623-543)
    chapter12 = writer.add_bookmark('Chapter 12: Vectors, Curves, and Surfaces in Space', 707-543)
    chapter13 = writer.add_bookmark('Chapter 13: Partial Differentiation', 795-543)
    chapter14 = writer.add_bookmark('Chapter 14: Multiple Integrals', 885-543)
    chapter15 = writer.add_bookmark('Chapter 15: Vector Calculus', 959-543)
    appendices = writer.add_bookmark('Appendices', 477+1)


    # 10. Polar Coordinates And Plane Curves
    writer.add_bookmark('10.1 Analytic Geometry and the Conic Sections', 568-543, parent=chapter10)
    writer.add_bookmark('10.2 Polar Coordinates', 573-543, parent=chapter10)
    writer.add_bookmark('10.3 Area Computations in Polar Coordinates', 581-543, parent=chapter10)
    writer.add_bookmark('10.4 Parametric Curves', 586-543, parent=chapter10)
    writer.add_bookmark('10.5 Integral Computations with Parametric Curves', 595-543, parent=chapter10)
    writer.add_bookmark('10.6 The Parabola', 604-543, parent=chapter10)
    writer.add_bookmark('10.7 The Ellipse', 608-543, parent=chapter10)
    writer.add_bookmark('10.8 Hyperbola', 613-543, parent=chapter10)  

    # 11. Infinite Series
    writer.add_bookmark('11.1 Introduction', 624-543, parent=chapter11)
    writer.add_bookmark('11.2 Infinite Sequences', 624-543, parent=chapter11)
    writer.add_bookmark('11.3 Infinite Series and Convergence', 634-543, parent=chapter11)
    writer.add_bookmark('11.4 Taylor Series and Taylor Polynomials', 645-543, parent=chapter11)
    writer.add_bookmark('11.5 The Integral Test', 659-543, parent=chapter11)
    writer.add_bookmark('11.6 Comparison Tests for Positive-Term Series', 667-543, parent=chapter11)
    writer.add_bookmark('11.7 Alternating Series and Absolute Convergence', 673-543, parent=chapter11)
    writer.add_bookmark('11.8 Power Series', 682-543, parent=chapter11)
    writer.add_bookmark('11.9 Power Series Computations', 694-543, parent=chapter11)

    # 12. Vectors, Curves, and Surfaces in Space
    writer.add_bookmark('12.1 Vectors in the Plane', 708-543, parent=chapter12)
    writer.add_bookmark('12.2 Rectangular Coordinates and Three-Dimensional Vectors', 714-543, parent=chapter12)
    writer.add_bookmark('12.3 The Cross Product of Two Vectors', 725-543, parent=chapter12)
    writer.add_bookmark('12.4 Lines and Planes in Space', 733-543, parent=chapter12)
    writer.add_bookmark('12.5 Curves and Motion in Space', 742-543, parent=chapter12)
    writer.add_bookmark('12.6 Curvature and Acceleration', 757-543, parent=chapter12)
    writer.add_bookmark('12.7 Cylinders and Quadric Surfaces', 772-543, parent=chapter12)
    writer.add_bookmark('12.8 Cylindrical and Spherical Coordinates', 783-543, parent=chapter12)
    
    # 13. Partial Differentiation
    writer.add_bookmark('13.1 Introduction', 796-543, parent=chapter13)
    writer.add_bookmark('13.2 Functions of Several Variables', 796-543, parent=chapter13)
    writer.add_bookmark('13.3 Limits and Continuity', 806-543, parent=chapter13)
    writer.add_bookmark('13.4 Partial Derivatives', 812-543, parent=chapter13)
    writer.add_bookmark('13.5 Maxima and Minima of Functions of Several Variables', 823-543, parent=chapter13)
    writer.add_bookmark('13.6 Increments and Differentials', 835-543, parent=chapter13)
    writer.add_bookmark('13.7 The Chain Rule', 842-543, parent=chapter13)
    writer.add_bookmark('13.8 Directional Derivatives and the Gradient Vector', 853-543, parent=chapter13)
    writer.add_bookmark('13.9 Lagrange Multipliers and Constrained Maximum-Minimum Problems', 863-543, parent=chapter13)
    writer.add_bookmark('13.10 The Second Derivative Test for Functions of Two Variables', 873-543, parent=chapter13)

    # 14. Multiple Integrals
    writer.add_bookmark('14.1 Double Integrals', 886-543, parent=chapter14)
    writer.add_bookmark('14.2 Double Integrals over More General Regions', 893-543, parent=chapter14)
    writer.add_bookmark('14.3 Area and Volume by Double Integration', 899-543, parent=chapter14)
    writer.add_bookmark('14.4 Double Integrals in Polar Coordinates', 905-543, parent=chapter14)
    writer.add_bookmark('14.5 Applications of Double Integrals', 912-543, parent=chapter14)
    writer.add_bookmark('14.6 Triple Integrals', 924-543, parent=chapter14)
    writer.add_bookmark('14.7 Integration in Cylindrical and Spherical Coordinates', 932-543, parent=chapter14)
    writer.add_bookmark('14.8 Surface Area', 940-543, parent=chapter14)
    writer.add_bookmark('14.9 Change of Variables in Multiple Integrals', 946-543, parent=chapter14)

    # 15. Vector Calculus
    writer.add_bookmark('15.1 Vector Fields', 960-543, parent=chapter15)
    writer.add_bookmark('15.2 Line Integrals', 965-543, parent=chapter15)
    writer.add_bookmark('15.3 The Fundamental Theorem and Independence of Path', 976-543, parent=chapter15)
    writer.add_bookmark("15.4 Green's Theorem", 984-543, parent=chapter15)
    writer.add_bookmark('15.5 Surface Integrals', 993-543, parent=chapter15)
    writer.add_bookmark('15.6 The Divergence Theorem', 1004-543, parent=chapter15)
    writer.add_bookmark("15.7 Stokes' Theorem", 1011-543, parent=chapter15) 

    # Appendices
    writer.add_bookmark('A Real Numbers and Inequalities', 477+1, parent=appendices)
    writer.add_bookmark('B The Coordinate Plane and Straight Lines', 477+6, parent=appendices)
    writer.add_bookmark('C Review of Trigonometry', 477+14, parent=appendices)
    writer.add_bookmark('D Proofs of the Limit Laws', 477+20, parent=appendices)
    writer.add_bookmark('E The Completeness of the Real Number System', 477+26, parent=appendices)
    writer.add_bookmark('F Proof of the Chain Rule', 477+31, parent=appendices)
    writer.add_bookmark('G Existence of the Integral', 477+32, parent=appendices)
    writer.add_bookmark('H Approximations and Riemann Sums', 477+38, parent=appendices)
    writer.add_bookmark("I L'Hopital's Rule and Cauchy's Mean Value Theorem", 477+41, parent=appendices)
    writer.add_bookmark("J Proof of Taylor's Formula", 477+44, parent=appendices)
    writer.add_bookmark('K Conic Sections as Sections of a Cone', 477+45, parent=appendices)
    writer.add_bookmark('L Units of Measurement and Conversion Factors', 477+46, parent=appendices)
    writer.add_bookmark('M Formulas from Algebra, Geometry, and Trigonometry', 477+47, parent=appendices)
    writer.add_bookmark('N The Greek Alphabet', 477+49, parent=appendices)
        

    with open(output_pdf, "wb") as f_out:
        writer.write(f_out)

# 路径设置
input_pdf_path = 'Multivariable Calculus 5th.pdf'  # 输入文件路径
output_pdf_path = 'Multivariable Calculus 5th.pdf'    # 输出文件路径
add_hierarchical_bookmarks(input_pdf_path, output_pdf_path)

