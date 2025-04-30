before installing/updating this module

1) 

to be done in future

1) invoice preview after "Send & Print" make same as zatca report.
2) enterprise  report preview testing.

changelog

1) 16.11.x
   1) AV update completed.
   2) send to zatca via cron added as config.
   3) 
2) 16.10.x
    1) code modified for compatibility with tax inclusive prices
    2) ~~invoice level (document level) discount added as gift cards & promotions.~~
    3) invoice level (document level) discount added as -ve lines
    4) In simplified invoice, if partner.company_type == company, then 1000 SAR limit will be checked.
    5) current datetime added for compliance invoices.
   6) new configurations added in company
   6) simplified as A4 report
   7) header/footer remove from invoices, via config
   8) skip customer address validations added as config
   9) barcode added.
   10) new report template added.
   11) invoice line level allowance added.
   12) disable odoo invoice reports from print menu in tree & form
   13) PDF-A3 outlines, warning/error solved,
   14) Report invoice type modified for both
   15) tax exception reason (*), added in report lines.
3) 16.9.x
    1) code modified for compatibility with pre-payment module extension
    2) bt25 function separated.
    3) pos payment info added in simplified report
    4) invoice line & document level discount separated.
    5) remaining time added.
    6) invoice line made unique to each invoice.
4) 16.8.x
    1) auto compliance added.
5) 16.7.x
    1) translations, dashboard, self billed, arabic fields, reports
    2) (updated with arabic & self billed).
6) 16.6.x
    1) dashboard added.
7) 16.5.x
    1) self billed added.
