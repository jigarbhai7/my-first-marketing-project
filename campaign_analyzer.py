# Simple marketing data analyzer
import pandas as pd

def analyze_campaigns():
    print("📊 Welcome to Marketing Campaign Analyzer!")
    
    # Sample data (you'll replace this with real data later)
    campaigns = {
        'campaign': ['Social Media', 'Email', 'PPC'],
        'clicks': [1500, 800, 1200],
        'conversions': [75, 40, 60]
    }
    
    df = pd.DataFrame(campaigns)
    df['conversion_rate'] = (df['conversions'] / df['clicks'] * 100).round(2)
    
    print("\nCampaign Performance:")
    print(df)
    
    best_campaign = df.loc[df['conversion_rate'].idxmax()]
    print(f"\n🎯 Best Performing Campaign: {best_campaign['campaign']}")
    print(f"Conversion Rate: {best_campaign['conversion_rate']}%")

if __name__ == "__main__":
    analyze_campaigns()
