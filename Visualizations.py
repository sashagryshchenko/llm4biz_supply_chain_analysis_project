# %%
def visImports():
    import pandas as pd
    from openai import OpenAI
    ###from google.colab import userdata
    import EnvSettings as settings
    openai_key = settings.set_key() 
    client = OpenAI(api_key= openai_key)
    
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np

# Plotting the comparison
def plotResults():
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np
    criteria = ['Energy Source', 'Efficiency', 'Refueling Infrastructure', 'Emissions',
                'Supply Chain Complexity', 'Resource Use', 'Energy Storage',
                'Vehicle Range', 'Costs']
    fuel_cell_scores = [3, 2, 2, 3, 3, 2, 3, 3, 2]  # Example scores for fuel cell cars
    electric_vehicle_scores = [4, 5, 5, 4, 4, 5, 4, 4, 5]  # Example scores for electric vehicles
    bar_width = 0.35
    index = np.arange(len(criteria))

    plt.figure(figsize=(10, 6))
    plt.barh(index, fuel_cell_scores, bar_width, color='blue', label='Fuel Cell Cars')
    plt.barh(index + bar_width, electric_vehicle_scores, bar_width, color='orange', label='Electric Vehicles')
    plt.xlabel('Score')
    plt.yticks(index + bar_width / 2, criteria)
    plt.title('Supply Chain Comparison: Fuel Cell Cars vs Electric Vehicles')
    print("PlotResults Plotting")
    plt.legend()
    plt.show()
    return plt
# %%
def efficiencyComparison():
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np

    # Data for supply chain comparison
    criteria = ['Energy Source', 'Efficiency', 'Refueling Infrastructure', 'Emissions',
                'Supply Chain Complexity', 'Resource Use', 'Energy Storage',
                'Vehicle Range', 'Costs']
    fuel_cell_scores = [3, 2, 2, 3, 3, 2, 3, 3, 2]  # Example scores for fuel cell cars
    electric_vehicle_scores = [4, 5, 5, 4, 4, 5, 4, 4, 5]  # Example scores for electric vehicles
    print("efficiencyComparison Plotting")
    plt.legend()
    plt.show()
    ## save as png

# Data for environmental impact comparison
def envireImpactComparison(): 
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np   
    
    factors = ['Greenhouse Gas Emissions', 'Air Pollution', 'Energy Efficiency', 'Resource Use',
            'Infrastructure', 'Vehicle Range and Refueling', 'Cost', 'Water Emission', 'Lifecycle Analysis']
    fuel_cell_scores_env = [3, 3, 2, 2, 2, 3, 2, 3, 2]  # Example scores for fuel cell cars
    electric_vehicle_scores_env = [4, 4, 5, 4, 5, 4, 5, 4, 5]  # Example scores for electric vehicles
    # Plotting the comparison
    print("envireImpactComparison Plotting")
    bar_width = 0.35
    plt.figure(figsize=(12, 8))
    plt.show()
# Supply chain comparison
def supplyChainComparison():
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np   
    
    plt.barh(np.arange(len(criteria)) - bar_width/2, fuel_cell_scores, bar_width, color='blue', label='Fuel Cell Cars')
    plt.barh(np.arange(len(criteria)) + bar_width/2, electric_vehicle_scores, bar_width, color='orange', label='Electric Vehicles', alpha=0.6)
    print("supplyChainComparison Plotting")
    plt.legend()
    plt.show()
# Environmental impact comparison
def envireImpactElementsComparison():
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np   
   
    plt.barh(np.arange(len(factors)) - bar_width/2, fuel_cell_scores_env, bar_width, color='green', label='Fuel Cell Cars (Env)')
    plt.barh(np.arange(len(factors)) + bar_width/2, electric_vehicle_scores_env, bar_width, color='red', label='Electric Vehicles (Env)', alpha=0.6)

    plt.xlabel('Score')
    plt.yticks(np.arange(len(criteria)), criteria)
    plt.title('Supply Chain and Environmental Impact Comparison: Fuel Cell Cars vs Electric Vehicles')
    print("envireImpactElementsComparison Plotting")
    plt.legend()
    plt.show()
    plt.legend()
    plt.tight_layout()
    plt.show()
# %%
def suppyChainElementComparison():
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np   
    import Visualizations as vis
    # Data for supply chain element comparison
    features = ['Energy Source', 'Manufacturing of Energy Source', 'Vehicle Powertrain and Motor',
                'Manufacturing of Storage System', 'Energy Conversion and Efficiency',
                'Infrastructure for Refueling/Charging', 'Environmental Impact of Manufacturing',
                'Vehicle Lifespan and Maintenance']
    fuel_cell_scores = [3, 3, 2, 2, 3, 2, 3, 2]  # Example scores for fuel cell cars
    electric_vehicle_scores = [4, 4, 5, 4, 5, 4, 5, 4]  # Example scores for electric vehicles

    # Plotting the comparison
    bar_width = 0.35
    plt.figure(figsize=(12, 8))

    plt.barh(np.arange(len(features)) - bar_width/2, fuel_cell_scores, bar_width, color='purple', label='Fuel Cell Cars')
    plt.barh(np.arange(len(features)) + bar_width/2, electric_vehicle_scores, bar_width, color='yellow', label='Electric Vehicles', alpha=0.6)
   
    plt.xlabel('Score')
    plt.yticks(np.arange(len(features)), features)
    plt.title('Supply Chain Element Comparison: Fuel Cell Cars vs Electric Vehicles')
    plt.legend()
    plt.tight_layout()
    print("supplyChainElementComparison Plotting")
    plt.show()

