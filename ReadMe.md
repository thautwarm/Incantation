

# Incantation 


See [codes in Here](https://github.com/thautwarm/Incantation/tree/master/incantation)

This library is written by `flowpython`(so it just support Python 3.6.x now...), which makes the codes much more readable.
 

## A Simple Guide

```python

    from incantation.Module.CSS.Grid import container, col, row, grid
    from incantation.Module.CSS.Helpers import align, left_align, right_align, center_align
    from incantation.Module.abst import Seq
    
    main  = container()
    a_col = col("contents", grid(s=12) )

    a_row = row(Seq(a_col, a_col), name = "test_row")
    
    center_align(a_row)
    
    a_row.setIndent(2)
    
    print(a_row.gen())
    
    >>> """  
        <div name = "test_row" class = "center-align row">
            
                <div class = "col s12 m6 l4">
                    contents
                </div>

                <div class = "col s12 m6 l4">
                    contents
                </div>
          </div>
          """

    from incantation.Module.CSS.Table import table
    a_table = table(
        ["name", "email", "phone number"],
        [
            ["thautwarm","twshere@outlook.com",None],
            ["person1", "email1", "phone1"],
            ["deep","dark","fantasy"],
            ["Ass","Tol","Fo"]
        ]，
        action = "somescirpt"
    ) 
    a_table.gen() ->> print
    # print(a_table.gen())

    >>>     """
            <table action = "somescirpt">
                <thead>
                    <tr>
                    
                        <th>name</th>
                    
                        <th>email</th>
                    
                        <th>phone number</th>
                    
                    </tr>
                </thead>
                <tbody>
                    
                    <tr>
                        
                        <td>thautwarm</td>
                        
                        <td>twshere@outlook.com</td>
                        
                        <td>None</td>
                        
                </tr>
                    
                    <tr>
                        
                        <td>person1</td>
                        
                        <td>email1</td>
                        
                        <td>phone1</td>
                        
                </tr>
                    
                    <tr>
                        
                        <td>deep</td>
                        
                        <td>dark</td>
                        
                        <td>fantasy</td>
                        
                </tr>
                    
                    <tr>
                        
                        <td>Ass</td>
                        
                        <td>Tol</td>
                        
                        <td>Fo</td>
                        
                </tr>
                    
                </tbody>
            </table>
            """

    from incantation.template import Page
    
    
    from incantation.Module import blockquote   
    try_columns = blockquote("try columns")
    try_table   = blockquote("try tables") 
    main.contains(Seq(try_columns, a_row, try_table, a_table))
    page = Page(main)
    page.write(to = './test.html')

```

See `test.html`
![rendered `test.html`](https://github.com/thautwarm/Incantation/raw/master/test/testres.png)

