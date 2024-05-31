import mysql.connector
from datetime import datetime, timedelta

def get_customer_data():
    # Connect to the database
    connection = mysql.connector.connect(
        host='your_host',
        user='your_user',
        password='your_password',
        database='your_database'
    )
    
    cursor = connection.cursor(dictionary=True)
    
    # Query to get customer investment data
    query = "SELECT customer_id, investment_amount, investment_date, target_amount FROM investments"
    cursor.execute(query)
    
    data = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    return data

def calculate_sip_amount(investments):
    # Placeholder for SIP amount calculation logic
    # Example formula for SIP: A = P * [(1 + r/n)^(nt) - 1] / (r/n)
    # P = investment amount, r = annual interest rate, n = number of compounding periods per year, t = time in years
    sip_data = []
    for investment in investments:
        customer_id = investment['customer_id']
        P = investment['investment_amount']
        r = 0.1  # Assume an annual interest rate of 10%
        n = 12   # Monthly compounding
        t = 5    # Time in years for which SIP is calculated
        
        # Calculate SIP future value
        future_value = P * (((1 + r/n)**(n*t) - 1) / (r/n))
        
        # Calculate the time to reach the investment goal
        target_amount = investment['target_amount']
        months_to_goal = target_amount / future_value * 12
        
        investment_date = datetime.strptime(investment['investment_date'], '%Y-%m-%d')
        goal_date = investment_date + timedelta(days=months_to_goal * 30)  # Approximate months to days
        
        sip_data.append({
            'customer_id': customer_id,
            'sip_amount': future_value,
            'goal_date': goal_date
        })
    
    return sip_data

def main():
    customer_data = get_customer_data()
    sip_results = calculate_sip_amount(customer_data)
    
    for result in sip_results:
        print(f"Customer ID: {result['customer_id']}, SIP Amount: {result['sip_amount']:.2f}, Goal Date: {result['goal_date']}")

if __name__ == "__main__":
    main()
