# angular_distributions
Cross-section and angular distirbutions calculations at the Super Enge Split-Pole Spectrograph at FSU.

Run the code simply by running 'python3 angular_distribution_calculations.py'

The code expects BCI information stored in text files (currently supports up to 2 different isotopes, will be worked on to support any amount)
	BCI info should be stored as:   BCI hits     BCI Scale(nA)   --> in a two column list 
				i.e	  10000		   10
It also looks for directories that store the .txt files that hold the volume list for each peak of interest

The code loops through and calculates cross sections using the volume lists stored and will plot an angular distribution across all angles
	Two things: 1) if you do not have a volume measurement at an angle, leave a placeholder blank in at its angle
		    2) Right now it covers angles (15-60) in steps of 5 degrees, you can change the desired angles in the first line of the main() function

Angular Distributions will be shown in a grid of plots from smallest energy-->largest energy.
