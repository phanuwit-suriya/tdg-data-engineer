select transaction_date, name, email, mobile_no
from input_data
order by transaction_date;

insert into output_data (customer_sk, name, email, mobile_no, start_date, end_date, current_status_flag)
select row_number() over (order by t.name, t.transaction_date)          as customer_sk,
       t.name                                                           as name,
       t.email                                                          as email,
       regexp_replace(t.mobile_no, '(\d{2})(\d{4})(\d{4})', '\1-\2-\3') as mobile_no,
       t.transaction_date                                               as start_date,
       case when t.next_transaction_date is null
            then '2999-01-01'
            else t.next_transaction_date end                            as end_date,
       t.next_transaction_date is null                                  as current_status_flag
from (
  select transaction_date,
         name,
         email,
         mobile_no,
         lead(transaction_date) over (partition by name order by transaction_date) as next_transaction_date
  from input_data
) t;

select customer_sk, name, email, mobile_no, start_date, end_date, current_status_flag
from output_data
order by customer_sk;