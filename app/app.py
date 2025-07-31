# Import necessary libraries for the dashboard
import seaborn as sns
from faicons import icon_svg  # For Font Awesome icons in value boxes
from shiny import reactive     # Reactive programming support
from shiny.express import input, render, ui  # Shiny UI components
import palmerpenguins          # Penguins dataset

# Load penguins dataset into a DataFrame
df = palmerpenguins.load_penguins()

# Set dashboard page options with title and fillable layout
ui.page_opts(title="Module 7 Penguins Dashboard - Blessing", fillable=True)

# Sidebar UI with filters and helpful links
with ui.sidebar(title="Filter controls - Blessing"):

    # Slider input to filter by body mass (grams)
    ui.input_slider("mass", "Mass (body mass in grams)", 2000, 6000, 6000)

    # Checkbox group input to filter penguin species
    ui.input_checkbox_group(
        "species",
        "Species",
        ["Adelie", "Gentoo", "Chinstrap"],
        selected=["Adelie", "Gentoo", "Chinstrap"],
    )

    ui.hr()  # Horizontal line for separation

    # Useful links related to the project and PyShiny
    ui.h6("Links")
    ui.a("GitHub Source (Mine)", href="https://github.com/teflxndxn/cintel-07-tdash", target="_blank")
    ui.a("GitHub App (Mine)", href="https://teflxndxn.github.io/cintel-07-tdash/", target="_blank")
    ui.a("GitHub Issues (Mine)", href="https://github.com/teflxndxn/cintel-07-tdash/issues", target="_blank")
    ui.a("PyShiny", href="https://shiny.posit.co/py/", target="_blank")
    ui.a("Template: Basic Dashboard", href="https://shiny.posit.co/py/templates/dashboard/", target="_blank")
    ui.a("My LinkedIn", href="https://www.linkedin.com/in/blessing-aganaga-ms-bsc-641928353/", target="_blank")

# Value boxes showing summary statistics about filtered penguins
with ui.layout_column_wrap(fill=False):

    # Number of penguins displayed
    with ui.value_box(showcase=icon_svg("earlybirds")):
        "Number of penguins"

        @render.text
        def count():
            return filtered_df().shape[0]

    # Average bill length (mm)
    with ui.value_box(showcase=icon_svg("ruler-horizontal")):
        "Average bill length (mm)"

        @render.text
        def bill_length():
            return f"{filtered_df()['bill_length_mm'].mean():.1f} mm"

    # Average bill depth (mm)
    with ui.value_box(showcase=icon_svg("ruler-vertical")):
        "Average bill depth (mm)"

        @render.text
        def bill_depth():
            return f"{filtered_df()['bill_depth_mm'].mean():.1f} mm"

# Main content area with charts and data grid
with ui.layout_columns():

    # Scatter plot of bill length vs bill depth colored by species
    with ui.card(full_screen=True):
        ui.card_header("Bill Length vs. Depth Scatter Plot")

        @render.plot
        def length_depth():
            return sns.scatterplot(
                data=filtered_df(),
                x="bill_length_mm",
                y="bill_depth_mm",
                hue="species",
                palette={
                    "Adelie": "purple",
                    "Gentoo": "orange",
                    "Chinstrap": "green"
                }
            )

    # Interactive data grid showing key penguin measurements
    with ui.card(full_screen=True):
        ui.card_header("Interactive Penguin Data Grid")

        @render.data_frame
        def summary_statistics():
            cols = [
                "species",
                "island",
                "bill_length_mm",
                "bill_depth_mm",
                "body_mass_g",
            ]
            return render.DataGrid(filtered_df()[cols], filters=True)

# Server-side reactive logic to filter data based on inputs
@reactive.calc
def filtered_df():
    filt_df = df[df["species"].isin(input.species())]
    filt_df = filt_df.loc[filt_df["body_mass_g"] < input.mass()]
    return filt_df
