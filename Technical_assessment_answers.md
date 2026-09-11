
## Answer to "What do you have to do to get to zero target variance?" question

From the given table, we can see that MSFT, AAPL and HD already have zero target variance.
So, we leave them as-is. Focus on IBM and ORCL securities. ORCL securities worth of target variance 10% needs to be sold,
while we need to purchase 10% of target variance in IBM securities. Having a total 100_000 USD, we know that currently ORCL
accounts for 30% -> 30_000, so we sell 10_000 worth of ORCL securities. The amount of money we get from this trade is later
used to purchase IBM securities, which covers the negative 10% target variance.

Having the following assumptions, we can build a simple algorithm:
 - we are not considering transaction fees while doing sell/buy operations
 - the unit price of each security is constant and does not change during the sell/buy operations
 - In the problem description it was not mentioned what should happen when there won't be enough cash (money) to 
   re-balance, or when free cash left after re-balancing.. In the program I developed I am simply
   printing the leftover cash, if the cash is negative, i.e. account would go in debt due to rebalancing then 
   we fail the test with an appropriate error message
 - We assume that we always want to evently distribute the total assets, i.e. If we have 5 securities, we want to 
   have 20% of total assets in each security. If there is 3 securities -> 33.33% and etc..
 - We assume that all trade happens in the single currenct USD. No currency conversion is considered.
 - To make this document readable, we take only 2 digits after the floating point. In real production platforms, 
   we would use a more precise representation of the floating point numbers because they make up large sum at scale.


## Answer to the "Output - Number of shares to buy/sell" in the table

We have to sell 45.45 shares of ORCL -> ORCL currently accounts for 30% of total assest, so a 10% target variance 
gives us 10_000 USD. Considering ORCL unit price 220, we get 10_000 / 220 = 45.45 shares.
And buy 66.67 shares of IBM.

| Security | target% | current% | target variance% | unit price | Number of shares to buy/sell |
|----------|---------|----------|------------------|------------|------------------------------|
| IBM      | 20      | 10       | -10              | 150        | 66.67 (buy)                  |
| MSFT     | 20      | 20       | 0                | 90         | 0                            |
| ORCL     | 20      | 30       | 10               | 220        | 45.45 (sell)                 |
| AAPL     | 20      | 20       | 0                | 450        | 0                            |
| HD       | 20      | 20       | 0                | 300        | 0                            |



## Test cases

## Functional tests (Equivalence Partitioning, Boundary Value analysis, positive and negative scenarios)

### TC1: Rebalance the portfolio in happy path scenario
   - Objective: Verify that a given valid portfolio can be re-balanced correctly
   - Test Data: [tc01_happy_path.csv](tests/test_data/tc01_happy_path.csv)
   - Expected Result: Portfolio evenly re-balanced

### TC2: Rebalance the portfolio when a single security holds 100% of total assets
   - Objective: Verify that portfolio can be evenly re-balanced, despite initially a single security accounting for all 100% of assets
   - Test Data: [tc02_one_security_holds_all_assets.csv](tests/test_data/tc02_one_security_holds_all_assets.csv)
   - Expected Result: Portfolio evenly re-balanced

### TC3: Reject portfolio re-balancing when the unit price of a security is negative
   - Objective: Verify that data validation checks appropriately handle unexpected values
   - Test Data: [tc03_negative_unit_price.csv](tests/test_data/tc03_negative_unit_price.csv)
   - Expected Result: Appropriate error message is returned

### TC4: Reject portfolio re-balancing when the unit price of a security is zero
   - Objective: Verify that data validation checks appropriately handle unexpected values
   - Test Data: [tc04_zero_unit_price.csv](tests/test_data/tc04_zero_unit_price.csv)
   - Expected Result: Appropriate error message is returned

### TC5: Reject portfolio re-balancing when the target variance of a security > 100, e.g. 110
   - Objective: Verify that appropriate error message returned and application doesn't crash when a security 
     target variance is greater than 100, a negative test handled appropriately   
   - Test Data: [tc05_target_variance_above_100.csv](tests/test_data/tc05_target_variance_above_100.csv)
   - Expected Result: Appropriate error message is returned

### TC6: Reject portfolio re-balancing when the target variance of a security < -100, e.g. -110
   - Objective: Verify that appropriate error message returned and application doesn't crash when a security
     target variance is less than -100, a negative test handled appropriately
   - Test Data: [tc06_target_variance_below_minus_100.csv](tests/test_data/tc06_target_variance_below_minus_100.csv)
   - Expected Result: Appropriate error message is returned


### TC7: Reject portfolio re-balancing when there are no securities, empty table
   - Objective: Verify that appropriate error message returned and application doesn't crash when an empty portfolio is provided
   - Test Data: [tc07_no_securities.csv](tests/test_data/tc07_no_securities.csv)
   - Expected Result: Appropriate error message is returned

### TC8: Rebalance the portfolio when the unit price of security is a floating point number, e.g, 39.57
   - Objective: Verify that portfolio can be correctly re-balanced when a security has a floating point unit price
   - Test Data: [tc08_floating_point_unit_price.csv](tests/test_data/tc08_floating_point_unit_price.csv)
   - Expected Result: Portfolio evenly re-balanced and the number of shares to buy/sell calculated correctly

### TC9: Re-balancing with floating point numbers. Total securities count is 3 (which gives floating point 33.33333% for each security for re-balancing)
   - Objective: Verify that floating point target percentages are calculated and handled correctly when the portfolio cannot be evenly divided using whole numbers
   - Test Data: [tc09_floating_point_rebalancing.csv](tests/test_data/tc09_floating_point_rebalancing.csv)
   - Expected Result: Portfolio evenly re-balanced and floating point calculations handled with appropriate precision

### TC10: Rebalance the portfolio when a single security unit price is greater than the total portfolio value
A security currently accounts for 0%, target variance is 20% but a unit price of security is > 100_000, e.g. 110_000

   - Objective: Verify that portfolio can be re-balanced correctly when the unit price of a security is greater than the total portfolio value
   - Test Data: [tc10_unit_price_above_portfolio_value.csv](tests/test_data/tc10_unit_price_above_portfolio_value.csv); the portfolio is also shown in the table below
   - Expected Result: Portfolio evenly re-balanced and the fractional number of shares to buy calculated correctly

### TC11: Rebalance the portfolio when it is already evenly balanced
   - Objective: Verify that no buy/sell operations are performed when the portfolio is already evenly balanced
   - Test Data: [tc11_already_balanced.csv](tests/test_data/tc11_already_balanced.csv)
   - Expected Result: Number of shares to buy/sell is zero for every security

### TC12: Rebalance the portfolio when target percentage is zero for one of the securities
   - Objective: Verify that portfolio re-balancing correctly handles a security with a zero target percentage
   - Test Data: [tc12_zero_target_percentage.csv](tests/test_data/tc12_zero_target_percentage.csv)
   - Expected Result: The security with zero target percentage is fully sold and the portfolio is re-balanced according to the remaining target percentages

### TC13: Rebalance the portfolio when free cash is left after re-balancing
   - Objective: Verify that application correctly calculates and reports any free cash left after re-balancing the portfolio
   - Test Data: [tc13_free_cash_after_rebalancing.csv](tests/test_data/tc13_free_cash_after_rebalancing.csv)
   - Expected Result: Portfolio re-balanced and the correct positive leftover cash amount is returned

### TC14: Reject rebalancing the portfolio when the account goes into debt after re-balancing
   Fail the test when due to re-balancing the if account goes in debt
   - Objective: Verify that application correctly calculates and reports when re-balancing causes the account to go into debt
   - Test Data: [tc14_debt_after_rebalancing.csv](tests/test_data/tc14_debt_after_rebalancing.csv)
   - Expected Result: Portfolio re-balance is rejected

### TC15: Rebalance the portfolio when it has a single security
   - Objective: Verify that a portfolio containing a single security can be processed correctly
   - Test Data: [tc15_single_security.csv](tests/test_data/tc15_single_security.csv)
   - Expected Result: The single security has a target percentage of 100% and no unnecessary buy/sell operations are performed

### TC16: Rebalance the portfolio when a security name contains non-ASCII characters
   - Objective: Verify that application can read and process a security name containing non-ASCII characters
   - Test Data: [tc16_non_ascii_security_name.csv](tests/test_data/tc16_non_ascii_security_name.csv)
   - Expected Result: Portfolio processed successfully and the security name is returned without corruption

### TC17: Reject portfolio re-balancing when total target percentage is greater than 100
   - Objective: Verify that appropriate error message returned and application doesn't crash when total target percentage is greater than 100
   - Test Data: [tc17_target_percentage_above_100.csv](tests/test_data/tc17_target_percentage_above_100.csv)
   - Expected Result: Appropriate error message is returned

### TC18: Reject portfolio re-balancing when total target percentage is less than 100
   - Objective: Verify that appropriate error message returned and application doesn't crash when total target percentage is less than 100
   - Test Data: [tc18_target_percentages_sum_below_100.csv](tests/test_data/tc18_target_percentages_sum_below_100.csv)
   - Expected Result: Appropriate error message is returned

### TC19: Reject portfolio re-balancing when current percentages don't sum up to 100, e.g. 80 or 110
   - Objective: Verify that appropriate error message returned and application doesn't crash when current percentages do not sum up to 100
   - Test Data: [tc19_current_percentages_sum_not_100.csv](tests/test_data/tc19_current_percentages_sum_not_100.csv)
   - Expected Result: Appropriate error message is returned

### TC20: Reject portfolio re-balancing when a duplicate security exists
   - Objective: Verify that data validation checks appropriately handle duplicate securities in the portfolio
   - Test Data: [tc20_duplicate_security.csv](tests/test_data/tc20_duplicate_security.csv)
   - Expected Result: Appropriate error message is returned and portfolio is not re-balanced

### TC21: Reject portfolio re-balancing when the portfolio table has empty cells
   - Objective: Verify that data validation checks appropriately handle empty required fields in the portfolio table
   - Test Data: [tc21a_empty_security.csv](tests/test_data/tc21a_empty_security.csv),
     [tc21b_empty_target.csv](tests/test_data/tc21b_empty_target.csv),
     [tc21c_empty_current.csv](tests/test_data/tc21c_empty_current.csv),
     [tc21d_empty_target_variance.csv](tests/test_data/tc21d_empty_target_variance.csv),
     [tc21e_empty_unit_price.csv](tests/test_data/tc21e_empty_unit_price.csv),
     [tc21f_multiple_empty_cells_one_row.csv](tests/test_data/tc21f_multiple_empty_cells_one_row.csv),
     [tc21g_multiple_empty_cells_across_rows.csv](tests/test_data/tc21g_multiple_empty_cells_across_rows.csv), and
     [tc21h_completely_empty_row.csv](tests/test_data/tc21h_completely_empty_row.csv)
   - Expected Result: Appropriate error message is returned and application doesn't crash


## Security tests

### TC22: Reject portfolio re-balancing when SQL injection is entered in any field
   - Objective: Verify that malicious SQL input is handled safely and cannot execute SQL commands or affect stored data
   - Test Data: [tc22_sql_injection.csv](tests/test_data/tc22_sql_injection.csv)
   - Expected Result: Malicious input is rejected or safely treated as plain text and no SQL command is executed

### TC23: Reject portfolio re-balancing when any field contains a null value
   - Objective: Verify that data validation checks appropriately handle null values in any required field
   - Test Data: [tc23_null_values.csv](tests/test_data/tc23_null_values.csv)
   - Expected Result: Appropriate error message is returned and application doesn't crash

### TC24: Reject portfolio re-balancing when any field contains a malformed value
   - Objective: Verify that data validation checks appropriately handle values that do not match the expected field type or format
   - Test Data: [tc24_malformed_values.csv](tests/test_data/tc24_malformed_values.csv)
   - Expected Result: Appropriate error message is returned and application doesn't crash


## Load tests

### TC25: Reject portfolio re-balancing when a number in any field causes an overflow
   - Objective: Verify that application handles numbers outside the supported range without overflowing or crashing
   - Test Data: [tc25_number_overflow.csv](tests/test_data/tc25_number_overflow.csv)
   - Expected Result: Appropriate error message is returned and no incorrect calculation is performed

### TC26: Rebalance the portfolio when it contains an extremely large number of securities
   - Objective: Verify that application remains stable while reading and processing a portfolio containing an extremely large number of securities
   - Test Data: [tc26_extremely_large_security_count.csv](tests/test_data/tc26_extremely_large_security_count.csv)
   - Expected Result: Portfolio is processed within acceptable resource limits, or an appropriate size limit error message is returned without the application crashing
