import pandas as pd
import pymysql

# Load CSV
df = pd.read_csv("sql/fake_data.csv")
df.fillna('', inplace=True)

# Connect to MySQL
conn = pymysql.connect(
    host="localhost",
    user="db_user",
    password="6equj5_db_user",
    database="home_db",
    port=3306
)
cursor = conn.cursor()

for _, row in df.iterrows():
    # Insert into property table
    cursor.execute("""
        SELECT property_id FROM property WHERE address=%s AND zip=%s
    """, (row['Address'], row['Zip']))
    result = cursor.fetchone()

    if result:
        property_id = result[0]
    else:
        cursor.execute("""
            INSERT INTO property (
                title, address, street_address, city, state, zip, market, flood,
                property_type, highway, train, tax_rate, sqft_basement, htw, pool,
                commercial, water, sewage, year_built, sqft_mu, sqft_total, parking,
                bed, bath, basement_yes_no, layout, rent_restricted, neighborhood_rating,
                latitude, longitude, subdivision, school_average
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                      %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            row['Property_Title'], row['Address'], row['Street_Address'], row['City'], row['State'], row['Zip'],
            row['Market'], row['Flood'], row['Property_Type'], row['Highway'], row['Train'], row['Tax_Rate'],
            row['SQFT_Basement'], row['HTW'], row['Pool'], row['Commercial'], row['Water'], row['Sewage'],
            row['Year_Built'], row['SQFT_MU'], row['SQFT_Total'], row['Parking'], row['Bed'], row['Bath'],
            row['BasementYesNo'], row['Layout'], row['Rent_Restricted'], row['Neighborhood_Rating'],
            row['Latitude'], row['Longitude'], row['Subdivision'], row['School_Average']
        ))
        property_id = cursor.lastrowid

    # Insert into leads table
    cursor.execute("""
        INSERT INTO leads (property_id, reviewed_status, most_recent_status, occupancy,
                           net_yield, irr, selling_reason, seller_retained_broker,
                           final_reviewer, source)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        property_id, row['Reviewed_Status'], row['Most_Recent_Status'], row['Occupancy'],
        row['Net_Yield'], row['IRR'], row['Selling_Reason'], row['Seller_Retained_Broker'],
        row['Final_Reviewer'], row['Source']
    ))

    # Insert into valuation
    cursor.execute("""
        INSERT INTO valuation (property_id, previous_rent, list_price, zestimate, arv,
                               expected_rent, rent_zestimate, low_fmr, high_fmr, redfin_value)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        property_id, row['Previous_Rent'], row['List_Price'], row['Zestimate'], row['ARV'],
        row['Expected_Rent'], row['Rent_Zestimate'], row['Low_FMR'], row['High_FMR'], row['Redfin_Value']
    ))

    # Insert into hoa
    cursor.execute("""
        INSERT INTO hoa (property_id, hoa_amount, hoa_flag)
        VALUES (%s, %s, %s)
    """, (
        property_id, row['HOA'], row['HOA_Flag']
    ))

    # Insert into rehab
    cursor.execute("""
        INSERT INTO rehab (property_id, underwriting_rehab, rehab_calculation,
            paint_flag, flooring_flag, foundation_flag, roof_flag, hvac_flag,
            kitchen_flag, bathroom_flag, appliances_flag, windows_flag,
            landscaping_flag, trashout_flag)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        property_id, row['Underwriting_Rehab'], row['Rehab_Calculation'],
        bool(row['Paint']), bool(row['Flooring_Flag']), bool(row['Foundation_Flag']),
        bool(row['Roof_Flag']), bool(row['HVAC_Flag']), bool(row['Kitchen_Flag']),
        bool(row['Bathroom_Flag']), bool(row['Appliances_Flag']), bool(row['Windows_Flag']),
        bool(row['Landscaping_Flag']), bool(row['Trashout_Flag'])
    ))

    # Insert into taxes
    cursor.execute("""
        INSERT INTO taxes (property_id, taxes_amount)
        VALUES (%s, %s)
    """, (
        property_id, row['Taxes']
    ))

conn.commit()
cursor.close()
conn.close()
