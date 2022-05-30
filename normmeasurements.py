def normmeasurements(measurements, map):
  if map == 0:
    color = 'red'
    cmap = plt.cm.Reds
  if map == 1:
    color = 'green'
    cmap = plt.cm.Greens
  if map == 2:
    color = 'blue'
    cmap = plt.cm.Blues

  measurements2 = np.zeros((measurements.shape[0], 9))
  measurements2[:, 0] = measurements[:, 0]  # volume
  measurements2[:, 1] = measurements[:, 1] / measurements[:, 0]  # x coordinates
  measurements2[:, 2] = measurements[:, 2] / measurements[:, 0]  # y coordinates
  measurements2[:, 3] = measurements[:, 3] / measurements[:, 0]  # z coordinates
  measurements2[:, 4] = measurements[:, 10] / measurements[:, 0]  # I mean
  measurements2[:, 5] = np.sqrt(
    (measurements[:, 11] - (measurements[:, 10] / measurements[:, 0]) ** 2) / measurements[:,
                                                                              0])  # std I = sqrt(∑ (I² -(∑ I)²)/N'measurements2[:,6] = measurements[:,15]-(measurements[:,12])**2/measurements[:,10] # optical inertia about x Σ I (x-μx)² = Σ I x² - (Σ I x)²/Σ I
  measurements2[:, 6] = measurements[:, 18] - (measurements[:, 13]) ** 2 / measurements[:,
                                                                           10]  # optical inertia about y Σ I (x-μy)² = Σ I y² - (Σ I y)²/Σ I
  measurements2[:, 7] = measurements[:, 20] - (measurements[:, 14]) ** 2 / measurements[:,
                                                                           10]  # optical inertia about z Σ I (x-μz)² = Σ I z² - (Σ I z)²/Σ I
  measurements2[:, 8] = measurements[:, 21]  # max I

  if saveimages:
    columns = measurements2.shape[1]
    rows = measurements2.shape[1]
    fig, ax_array = plt.subplots(rows, columns, squeeze=False,
                                 gridspec_kw={'hspace': 0, 'wspace': 0})  # sharex = True, sharey = True,
    for i, ax_row in enumerate(ax_array):  # reversed(list(enumerate(ax_array))):
      for j, axes in reversed(list(enumerate(ax_row))):
        # axes.set_title('{},{}'.format(i,j))
        # if i != rows:
        if j == 0:
          # axes.set_xticklabels([])
          axes.get_xaxis().set_visible(True)
          axes.get_yaxis().set_visible(True)
        elif i == rows - 1:
          axes.get_xaxis().set_visible(True)
          axes.get_yaxis().set_visible(False)
        else:
          axes.set_xticklabels([])
          axes.set_yticklabels([])
          axes.get_xaxis().set_visible(False)
          axes.get_yaxis().set_visible(False)
        axes.get_xaxis().set_visible(False)
        axes.get_yaxis().set_visible(False)

        # if j == 0:
        # axes.set_yticklabels([])
        # axes.get_yaxis().set_visible(False)
        # plt.setp(axes.get_xticklabels(), visible=False)
        # plt.setp(axes.get_yticklabels(), visible=False)
        # plt.setp(ax[i,j].get_xticklabels(), visible=False)
        # axes.scatter(measurements[:][i],measurements[:][j])

        # if i == j+1:
        # # axes.hist(measurements2[:,i],15, color = "steelblue")

        if i == j:

          try:
            (counts, bins) = np.histogram(measurements2[:, i], bins=20)
            factor = np.max(measurements2[:, i]) / np.max(counts)
          except:
            factor = 1
          axes.hist(bins[:-1], bins, weights=factor * counts, color=color)
          # axes.hist(measurements2[:,i],20, color = "steelblue")
          # axes.set_ylim([np.min(measurements2[:,j]), np.max(measurements2[:,j])])
          # counts, binEdges=np.histogram(measurements2[:,i],bins=20)
          # axes.bar(binEdges[1:],counts*np.max(measurements[:,i])/np.max(counts), color = "steelblue")
        else:
          # # axes.hist2d(measurements2[:,i],measurements2[:,j], cmap=plt.cm.Blues)
          try:
            axes.hist2d(measurements2[:, j], measurements2[:, i], cmap=cmap)
          except:
            pass
    plt.savefig(filename + 'stats.png')
    if show:
      plt.show()
    else:
      plt.close()

  return measurements2
