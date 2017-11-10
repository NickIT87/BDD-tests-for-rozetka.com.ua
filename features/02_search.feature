Feature: I want check search field

 Scenario Outline: Search complete
    Given I am on home page
    then I search for <product> 
    when I should see results <search_count> 

 Examples: By product name
    | product     | search_count |
    | notebooks   | 32           |

 Scenario Outline: Search fail
    then I search for <invalid_request> 
    when I should see results <not_found>

 Examples: By invalid name
    | invalid_request | not_found                                     |
    | sdfgsdfgdfsg    | ничего не найдено, попробуйте изменить запрос |