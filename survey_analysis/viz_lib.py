'''
Visualization tools for plotting probability data

* bar : Creates a bar chart of data
* plot_reasons : plots the reasons the input student did not take calc 2

'''

import matplotlib.pyplot as plt
import numpy as np


def bar(x, y, title, xlabel, ylabel, file_name):
    '''
    Creates a bar chart

    Parameters
    ----------
    x : The names for the x axis

    y : The values for each x item

    title : The title of the plot

    xlabel : The lable for the x-axis

    ylabel : The label for the y-axis

    file_name : The name of the file to save

    Returns
    -------
    None, creates a bar chart in current directory
    '''
    # use a unique color for the input student bar
    colors = []
    for i in range(len(x)):
        if i == 0:
            colors.append('rebeccapurple')
        else:
            colors.append('mediumpurple')

    fig = plt.figure()
    plt.bar(x, y, color=colors)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.savefig(file_name)

    return None


def plot_reasons(all_, filt_, output_file):
    '''
    Creates a double bar chart

    Parameters
    ----------
    all_resp : Dataset with all respondents

    filt_resp : Dataset with filtered respondents

    output_file : The name of the file to save

    Returns
    -------
    None, creates a double bar chart in current directory
    '''

    # Remove respondents who are taking Calculus 2
    all_ = all_[all_.reason != 'n/a - I am taking Calculus II.']
    filt_ = filt_[filt_.reason != 'n/a - I am taking Calculus II.']

    # Find the counts for each reason the student is not taking calc 2
    reason_counts_filt = []
    reason_counts_all = []

    # define all possible reasons
    reasons = [
      'I changed my major and now do not need to take Calculus II.',
      'My experience in Calculus I made me decide not to take Calculus II.',
      '"To do well in Calculus II, I would need to spend more time and' +
      'effort than I can afford."',
      'My grade in Calculus I was not good enough to continue to' +
      'Calculus II.',
      'Other:',
      'It is not required for my major / I have too many other courses' +
      'that I need to complete.',
      "I don't think I understand the ideas of Calculus I well enough to" +
      "take Calculus II."]

    # find the number of times each reason occurs
    for i in reasons:
        if i in filt_.reason.unique():
            reason_counts_filt.append(filt_.reason.value_counts()[i])
        else:
            reason_counts_filt.append(0)
        if i in all_.reason.unique():
            reason_counts_all.append(all_.reason.value_counts()[i])
        else:
            reason_counts_all.append(0)

    # save as array so we can do math later
    all_counts = np.array(reason_counts_filt)
    filt_counts = np.array(reason_counts_all)

    # create the plot
    fig, axs = plt.subplots(nrows=2,
                            ncols=1,
                            figsize=(12, 8),
                            gridspec_kw={'height_ratios': [2, 1]})

    # define axes
    ax0 = axs[0]
    ax1 = axs[1]

    # find ttl number of students not taking calc 2
    num_all = all_counts.sum()
    num_filt = filt_counts.sum()

    # plot the bar charts for both the filtered student and all respondents
    ax0.bar(x=np.arange(0, 7)-0.2,
            height=(filt_counts/num_filt)*100,
            label='filtered respondents',
            width=0.4,
            color='rebeccapurple')
    ax0.bar(x=np.arange(0, 7)+0.2,
            height=(all_counts/num_all)*100,
            label='All respondents',
            width=0.4,
            color='mediumpurple')

    # Customize ticks and labels
    ax0.set_xticks(np.arange(0, 7))
    ax0.set_xticklabels(np.arange(1, 8))
    ax0.set_xlabel('Reason for not taking calculus 2', fontsize=16)
    ax0.set_ylabel('Percentage of responses', fontsize=16)
    ax0.set_title("Responses to Why arent you taking Calculus 2?", fontsize=20)

    ax0.legend()

    # Now add the caption using the second axis
    ax1.axis('off')
    ax1.text(
      0,
      0.01,
      'Reason 1: I changed my major and now do not need to take Calculus II.' +
      '\n' +
      'Reason 2: My experience in Calculus I made me decide not to take' +
      'Calculus II. \n' +
      'Reason 3: To do well in Calculus II, I would need to spend more time' +
      'and effort than I can afford. \n' +
      'Reason 4: My grade in Calculus I was not good enough to continue to' +
      'Calculus II. \n' +
      'Reason 5: Other: \n' +
      'Reason 6: It is not required for my major / I have too many other' +
      'courses that I need to complete. \n' +
      "Reason 7: I don't think I understand the ideas of Calculus I well" +
      'enough to take Calculus II. \n',
      fontsize=13)

    plt.savefig(f"{output_file}")

    return None
