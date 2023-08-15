import bar_chart_race as bcr
import pandas as pd

df = pd.read_csv("/Users/davidjiang/cs/fun/elo/cumelo/CCWT.csv", index_col = "Games")
df.fillna(0.0, inplace = True)
# df = bcr.load_dataset('/Users/davidjiang/cs/fun/elo/cumelo/dete2.csv')
bcr.bar_chart_race(
    df=df,
    filename='scibowl.mp4',
    orientation='h',
    sort='desc',
    n_bars=15,
    fixed_order=False,
    fixed_max=True,
    steps_per_period=10,
    interpolate_period=False,
    label_bars=True,
    bar_size=1,
    period_length=640,
    figsize=(16, 10),
    dpi=144,
    cmap='dark12',
    title='Scibowl Elos',
    title_size='',
    bar_label_size=16,
    tick_label_size=14,
    shared_fontdict={'family' : 'Helvetica', 'color' : '.1'},
    scale='linear',
    writer=None,
    fig=None,
    bar_kwargs={'alpha': .7},
    filter_column_colors=False)  