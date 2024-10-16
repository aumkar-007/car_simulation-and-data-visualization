import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st
from sklearn.cluster import KMeans
from sklearn.ensemble import IsolationForest

def plot_speed_distribution(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df['speed'], kde=True, color='blue', bins=30)
    plt.title('Speed Distribution (with KDE)', fontsize=14)
    plt.xlabel('Speed', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    st.pyplot(plt.gcf())

def plot_speed_vs_acceleration(df):
    plt.figure(figsize=(10, 6))
    sns.regplot(x='acceleration', y='speed', data=df, scatter_kws={'s': 10}, line_kws={"color": "red"})
    plt.title('Speed vs Acceleration', fontsize=14)
    plt.xlabel('Acceleration', fontsize=12)
    plt.ylabel('Speed', fontsize=12)
    st.pyplot(plt.gcf())

    # Heatmap
    plt.figure(figsize=(10, 6))
    sns.kdeplot(x=df['acceleration'], y=df['speed'], cmap="Blues", fill=True)
    plt.title('Heatmap of Speed vs Acceleration', fontsize=14)
    plt.xlabel('Acceleration', fontsize=12)
    plt.ylabel('Speed', fontsize=12)
    st.pyplot(plt.gcf())

def plot_polar_direction(df):
    plt.figure(figsize=(8, 8))
    ax = plt.subplot(111, projection='polar')
    ax.scatter(np.radians(df['direction']), df['speed'], alpha=0.75, c='blue', s=10)
    plt.title('Speed vs Direction (Polar Plot)', fontsize=14)
    st.pyplot(plt.gcf())


def plot_proximity(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['proximity'], color='purple')
    plt.title('Proximity Over Time', fontsize=14)
    plt.xlabel('Index', fontsize=12)
    plt.ylabel('Proximity', fontsize=12)
    st.pyplot(plt.gcf())

def perform_clustering(df):
    # Select features for clustering
    X = df[['speed', 'acceleration', 'direction']]

    # Perform K-Means clustering
    kmeans = KMeans(n_clusters=3)
    df['cluster'] = kmeans.fit_predict(X)

    # Visualize clusters
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='speed', y='acceleration', hue='cluster', data=df, palette='Set1')
    plt.title('Clusters of Driving Patterns')
    plt.xlabel('Speed')
    plt.ylabel('Acceleration')
    st.pyplot(plt.gcf())


def detect_anomalies(df):
    # Select relevant features for anomaly detection
    X = df[['speed', 'acceleration', 'proximity']]

    # Apply Isolation Forest
    iso_forest = IsolationForest(contamination=0.01)
    df['anomaly'] = iso_forest.fit_predict(X)

    # Visualize anomalies
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='speed', y='acceleration', hue='anomaly', data=df, palette='Set2')
    plt.title('Anomalies in Driving Patterns')
    plt.xlabel('Speed')
    plt.ylabel('Acceleration')
    st.pyplot(plt.gcf())