import tensorflow as tf
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
st.title("Risk Aware Assessment")
st.sidebar.title("Upload probabilities")

# Defining generalised mean functions
def decisiveness(x):
    # Decisiveness = Arithmetic mean
    result = tf.reduce_mean(x) 
    return result.numpy()
    
def accuracy(x):
    # Accuracy = Geometric mean
    n = len(x)
    result = tf.math.exp(tf.reduce_sum(tf.math.log(x)/n))
    return result.numpy()

def robustness(x):
    # Robustness = -2/3 Mean
    n = len(x)
    result = tf.reduce_sum((x ** (-2/3))/n) ** (-3/2)
    return result.numpy()

#Disabling warning
st.set_option('deprecation.showfileUploaderEncoding', False)
#Choose your own image
uploaded_file = st.sidebar.file_uploader(" ",type=['csv'] )

if uploaded_file is not None:
    x = np.genfromtxt(uploaded_file, delimiter=',')
    
    # converting probabilities to log scale
    x_log_prob = np.log(x)
    
    decisiveness_x = decisiveness(x)
    accuracy_x = accuracy(x)
    robustness_x = robustness(x)
    
    col1, col2, col3 = st.columns(3)
    col1.metric('Accuracy', f'{accuracy_x:0.3e}')
    col1.metric('Decisiveness', f'{decisiveness_x:0.3e}')
    col1.metric('Robustness', f'{robustness_x:0.3e}')
    
    fig, ax = plt.subplots(figsize=(16, 12))
    
    # Plot in logscale, so convert the metric as logs as well
    log_dec = np.log(decisiveness_x)
    log_acc = np.log(accuracy_x)
    log_rob = np.log(robustness_x)
    
    dec_txt = f'{decisiveness_x:0.2e}'
    acc_txt = f'{accuracy_x:0.2e}'
    rob_txt = f'{robustness_x:0.2e}'
    
    # Adding the generalised mean values to the plot
    plt.axvline(log_dec, color='r', linestyle='dashed', linewidth=2)
    plt.text(log_dec, 10*12, dec_txt, color='r', size='large', weight='bold')
    plt.axvline(log_acc, color='b', linestyle='dashed', linewidth=2)
    plt.text(log_acc, 10*12, acc_txt, color='b', size='large', weight='bold')
    plt.axvline(log_rob, color='g', linestyle='dashed', linewidth=2)
    plt.text(log_rob, 10*12, rob_txt, color='g', size='large', weight='bold')
    
    # Plotting the histogram, inputs are log probabilities, frequencies are calculated on the log scale
    plt.hist(
                x_log_prob,
                log=True, 
                bins=100, 
                facecolor='white', 
                edgecolor='black'
                )
    
    # Adding labels
    plt.xlabel('Probabilities in log scale', fontdict = {'fontsize' : 20, 'weight': 'normal'})
    
    plt.ylabel(
        "Frequency in logscale", 
        fontdict = {'fontsize' : 20, 'weight': 'normal'}
        )
    
    # Converting ticks to probability scale post-hoc
    locs, labels = plt.xticks()
    locs = locs[:-1] # Don't need last tick mark
    prob_x_ticks = [np.exp(loc) for loc in locs]
    plt.xticks(locs, [f'{prob:0.0e}' for prob in prob_x_ticks])
    
    # Displaying plot in streamlit
    st.pyplot(fig)
    
    plt.savefig('hist.png')
    
    with open('hist.png', "rb") as img:
        btn = st.download_button(
            label="Download image",
            data=img,
            file_name='hist.png',
            mime="image/png"
        )
    
    
    