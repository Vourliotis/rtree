from rtree import *


def main():
    r_seed = 1
    np.random.seed(seed=r_seed)

    rtree = RTree()

    # VISUALIZATION SETTINGS
    # PLOT THE DATA IN A SEPERATE WINDOW
    plotData = True
    # PRINT THE DATA IN THE CONSOLE
    printInConsole = True

    # ENTRIES = POINTS FROM CSV FILE
    data_set = 'data'
    entries, time_elapsed_tree = rtree.import_csv(data_set)
    # ENTRIES = POINTS RANDOMLY CREATED WITH A SEED
    #entries, time_elapsed_tree = rtree.create_random_points(5, r_seed)

    # PRINT TREE IN CONSOLE
    if printInConsole == True:
        print(repr(rtree))

    if plotData == True:
        # PLOT ENTRIES
        plot_points(rtree, entries, False)
        # PLOT R-TREE
        rtree.show_points()

    # PRINT SKYLINE ENTRIES IN CONSOLE
    skyline, time_elapsed_skyline = rtree.bbs_skyline()
    if printInConsole == True:
        print("\nShowing Skyline Points:")
        for num_skylines in range(len(skyline)):
            print("")
            print(repr(skyline[num_skylines].mbr))

    if plotData == True:
        # SHOW SKYLINE WITHOUT THE TREE
        plot_points(rtree, entries, False, skyline)
        # PRINT SKYLINE IN R-TREE
        rtree.show_skyline(skyline)

    # RANGE QUERY IN R-TREE
    range_rec = Rectangle(Point(40, 40), Point(60, 60))
    query_entries, time_elapsed_query_entries = rtree.range_query(range_rec)

    # PRINT RANGE QUERY ENTRIES IN CONSOLE
    if printInConsole == True:
        print("\nShowing Range Query Points")
        for num_entries in range(len(query_entries)):
            print("")
            print(repr(query_entries[num_entries]))

    if plotData == True:
        # SHOW ENTRIES - POINTS
        plot_points(rtree, entries, False)
        # SHOW QUERY ENTRIES WITHOUT THE R-TREE
        plot_points(rtree, query_entries, True, None, range_rec)

    # RANGE QUERY SKYLINE ENTRIES IN CONSOLE
    skyline, time_elapsed_skyline_query = rtree.bbs_skyline_range_query(
        range_rec)
    if printInConsole == True:
        print("\nShowing Skyline Points given a range query:")
        for num_skylines in range(len(skyline)):
            print("")
            print(repr(skyline[num_skylines].mbr))

    if plotData == True:
        # SHOW ENTRIES - POINTS
        plot_points(rtree, entries, False)
        # SHOW SKYLINE ENTRIES GIVEN A RANGE QUERY
        plot_points(rtree, query_entries, False, skyline, range_rec)
        # SHOW SKYLINE ENTRIES GIVEN A RANGE QUERY IN THE R-TREE
        rtree.show_skyline(skyline)

    print("\nTime elapsed creating the tree: {:0.3f}s".format(
        time_elapsed_tree))
    print("Time elapsed finding the Skyline points: {:0.3f}s".format(
        time_elapsed_skyline))
    print("Time elapsed finding the range query entries: {:0.3f}s".format(
        time_elapsed_query_entries))
    print("Time elapsed finding the Skyline entries given a range: {:0.3f}s".format(
        time_elapsed_skyline_query))


def plot_points(rtree: RTree, entries: [Entry], show_block, skyline: [Entry] = None, range_rec=None):
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal')
    plt.xlim([rtree.root.mbr.lower_left.x - 10,
             rtree.root.mbr.upper_right.x + 10])
    plt.ylim([rtree.root.mbr.lower_left.y - 10,
             rtree.root.mbr.upper_right.y + 10])
    patches = []
    if range_rec is not None:
        ax.add_patch(matplotlib.patches.Rectangle((range_rec.lower_left.x, range_rec.lower_left.y),
                     range_rec.width, range_rec.height, fill=None, edgecolor='coral'))
    for i in range(len(entries)):
        ax.add_patch(plt.Circle(
            (entries[i].mbr.lower_left.x, entries[i].mbr.lower_left.y), 0.5, color='blue'))
    if skyline is not None:
        for i in range(len(skyline)):
            ax.add_patch(plt.Circle(
                (skyline[i].mbr.lower_left.x, skyline[i].mbr.lower_left.y), 0.5, color='coral'))
    plt.show(block=show_block)
    return True


if __name__ == '__main__':
    main()
