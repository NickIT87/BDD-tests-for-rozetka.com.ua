Feature: hover and click catalog link

 Scenario Outline: Search hover and choose
    Given I am on home page
    when find catalog i search for <product> and <search_request>
    then Check rubric headline and catalog btn <Header> next <product2> next <search_request2> next <Header2>
 
 Examples: By category
    | product               | search_request | Header                     | product2        | search_request2 | Header2           |
    | Ноутбуки и компьютеры | Комплектующие  | Компьютерные комплектующие | Бытовая техника | Кухня           | Техника для кухни |