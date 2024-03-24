import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import calendar

from Python_Files.Get_Functions import get_video_details, get_video_ids

def label_func(pct, allvals):
    absolute = int(pct/100.*sum(allvals))
    return f"{absolute}"



# MAIN FUNCTIONS -------------------------------------
def Statistics(video_ids):
    video_details = get_video_details(video_ids)
    video_df = pd.DataFrame(video_details)


    video_df['viewCount'] = pd.to_numeric(video_df['viewCount'])
    video_df['likeCount'] = pd.to_numeric(video_df['likeCount'])
    video_df['commentCount'] = pd.to_numeric(video_df['commentCount'])

    video_df['month name'] = video_df['publish_date'].apply(lambda x: calendar.month_name[int(x[5:7])])
    video_df['year'] = video_df['publish_date'].apply(lambda x: int(x[:4]))


    video_per_month = video_df.groupby('month name', as_index = False).size()

    sort_order = ['January', 'February','March','April', 'May', 'June' , 'July', 'August', 'September', 'October', 'November', 'December']

    video_per_month.index = pd.CategoricalIndex(video_per_month['month name'], categories=sort_order)

    video_per_index = video_per_month.sort_index()

    year_counts = video_df.groupby('year').size()

    # Optionally, you can sort the results by year
    year_counts = year_counts.sort_index()

    year_counts_dict = year_counts.to_dict()
    
    years = list(year_counts_dict.keys())
    counts = list(year_counts_dict.values())



    st.markdown('<h5 style="color: white; text-align : center">Top 10 Videos by Like Count From This Channel</h5>', unsafe_allow_html=True)

    # Get the top 10 videos by view count
    top_10_videos = video_df.sort_values(by='likeCount', ascending=False).head(10)

    # Create a list of titles and view counts
    titles = top_10_videos['Title'].tolist()
    like_counts = top_10_videos['likeCount'].tolist()

    # Bar plot using matplotlib

    with st.expander("View Chart"):
        st.success('Bar Plot:')
        fig, ax = plt.subplots()
        ax.bar(titles, like_counts)

        # Rotate the x-axis labels for readability
        plt.xticks(rotation=90)

        # Add title and labels
        ax.set_title('Top 10 Videos by Like Count')
        ax.set_xlabel('Video Title')
        ax.set_ylabel('Like Count')

        # Show plot in Streamlit
        st.pyplot(fig)


    st.markdown('<h5 style="color: white; text-align : center">Number of Videos Per Month</h5>', unsafe_allow_html=True)

    # Bar plot using matplotlib
    with st.expander("View Chart"):
        st.success('Bar Plot:')
        fig, ax = plt.subplots()
        ax.bar(video_per_index['month name'], video_per_index['size'])

        # Rotate xticks labels
        plt.xticks(rotation=90)

        # Add title and labels
        ax.set_title('Video per Month')
        ax.set_xlabel('Month Name')
        ax.set_ylabel('Size')

        # Show plot in Streamlit
        st.pyplot(fig)


    st.markdown('<h5 style="color: white; text-align : center">Video per Month in Pie Chart<h5>', unsafe_allow_html=True)

    
    with st.expander("View Chart"):
        col1, col2 = st.columns(2)

        with col1:
            # Pie chart using matplotlib
            st.success('Pie Chart 1:')
            fig, ax = plt.subplots()
            # ax.pie(video_per_index['size'], labels=video_per_index['month name'], autopct='%1.1f%%')
            ax.pie(video_per_index['size'], labels=video_per_index['month name'], autopct='%1.1f%%')

            # Add title
            ax.set_title('Video per Month in Percentage')

            # Show plot in Streamlit
            st.pyplot(fig)


        with col2:
        # Pie chart using matplotlib
            st.success('Pie Chart 2:')
            fig, ax = plt.subplots()
            ax.pie(video_per_index['size'], labels=video_per_index['month name'], autopct=lambda pct: label_func(pct, video_per_index['size']))

            # Add title
            ax.set_title('Video per Month in Count Wise')

            # Show plot in Streamlit
            st.pyplot(fig)


    # BAR PLOT FOR YEAR WISE -------------

    st.markdown('<h5 style="color: white; text-align : center">Number of Videos Year Wise</h5>', unsafe_allow_html=True)

    with st.expander("View Chart"):
        st.success("Bar Plot")
        start_year = min(years)
        end_year = max(years)
        all_years = range(start_year, end_year + 1)

        # Fill in missing years with zero counts
        filled_counts = [year_counts_dict.get(year, 0) for year in all_years]

        # Create bar plot
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.bar(all_years, filled_counts, color='skyblue')
        ax.set_xlabel('Year')
        ax.set_ylabel('Number of Videos')
        ax.set_title('Number of Videos Published by Year')
        plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

        # Add numbers above the bars
        for bar, count in zip(bars, filled_counts):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(count),
                    ha='center', va='bottom')

        # Show plot in Streamlit
        st.pyplot(fig)