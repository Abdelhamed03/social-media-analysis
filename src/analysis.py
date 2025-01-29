import matplotlib.pyplot as plt
import seaborn as sns

def analyze_all(df):
    """Generate all four plots in a single figure."""
    fig, axes = plt.subplots(2, 2, figsize=(20, 15))

    # 1️⃣ Post Type Performance Analysis (Top Left)
    avg_by_type = df.groupby('Type').agg({
        'Lifetime Post Total Reach': 'mean',
        'Lifetime Post Total Impressions': 'mean',
        'Lifetime Engaged Users': 'mean'
    }).round(2)

    normalized_metrics = avg_by_type.div(avg_by_type.max())
    normalized_metrics.plot(kind='bar', width=0.8, ax=axes[0,0])
    axes[0,0].set_title('Engagement Metrics by Post Type', fontsize=14, pad=20)
    axes[0,0].set_xlabel('Post Type', fontsize=12)
    axes[0,0].set_ylabel('Normalized Engagement', fontsize=12)
    axes[0,0].tick_params(axis='x', rotation=0)

    # 2️⃣ Timing Analysis (Top Right)
    hourly_engagement = df.groupby('Post Hour')['Lifetime Engaged Users'].mean().sort_index()
    axes[0,1].plot(hourly_engagement.index, hourly_engagement.values, marker='o', linewidth=2, markersize=8)
    axes[0,1].set_title('Average Engagement by Hour of Day', fontsize=14, pad=20)
    axes[0,1].set_xlabel('Hour of Day (24-hour format)', fontsize=12)
    axes[0,1].set_ylabel('Average Engaged Users', fontsize=12)
    axes[0,1].grid(True, alpha=0.3)
    axes[0,1].set_xticks(range(0, 24, 2))

    # 3️⃣ Paid vs Organic Performance (Bottom Left)
    paid_performance = df.groupby('Paid').agg({
        'Lifetime Post Total Reach': 'mean',
        'Lifetime Engaged Users': 'mean'
    }).round(2)
    paid_performance.index = ['Organic', 'Paid']
    paid_performance.plot(kind='bar', width=0.8, ax=axes[1,0])
    axes[1,0].set_title('Paid vs Organic Post Performance', fontsize=14, pad=20)
    axes[1,0].set_xlabel('Post Type', fontsize=12)
    axes[1,0].set_ylabel('Average Count', fontsize=12)
    axes[1,0].tick_params(axis='x', rotation=0)

    # 4️⃣ Category Performance (Bottom Right)
    category_performance = df.groupby('Category_Name')['Lifetime Engaged Users'].mean().sort_values(ascending=True)
    category_performance.plot(kind='barh', width=0.8, ax=axes[1,1])
    axes[1,1].set_title('Average Engagement by Category', fontsize=14, pad=20)
    axes[1,1].set_xlabel('Average Engaged Users', fontsize=12)
    axes[1,1].set_ylabel('Category', fontsize=12)

    
    plt.tight_layout(pad=3.0)

    # Display the plot
    plt.show()
