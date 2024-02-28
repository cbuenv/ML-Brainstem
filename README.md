# ML-Brainstem
This is a repository showcasing my work for the Depaul-Rosalind Franklin collaboration regarding the application of ML methodologies to delve into the organization and inner workings of the reticular formation.

## Introduction and Background
The brainstem is a complex and integral region of the brain itself, housing an intricate network of neurons that help regulate fundamental physiological functions, specifically vital orofacial motor behaviors. This includes, but is not limited to, the subconscious action of breathing, swallowing, vocalization/speech, and chewing. A disruption within said network, especially during fetal development, can lead to neurodevelopmental and neurodegenerative disorders such as central apneas, sudden infant death syndrome, dysphagia, and speech impediments. A major roadblock to learning more about these vital neural networks for possible future therapy is the fact that there is a lack of clear cytoarchitectonic boundaries and molecular markers that would otherwise demarcate possible regions for further study and/or medical intervention. The current understanding of how the brainstem, specifically the reticular formation, is undefined and lacking.

## Significance
The primary objective of this research effort is to conduct an in-depth investigation into the reticular formation based on gene expression data. This research effort aims to leverage machine learning methodologies to uncover latent relationships between genes, identify key players in the gene regulatory network, and ultimately contribute to a more nuanced comprehension of the brainstem’s role in vital physiological processes.

## Workflow
Below are summaries of the various research efforts I've conducted and led. Each effort is categorized as an individual "Operation". The summaries include any accompanying R/Python packages used in the analyses, as well as relevant input, output, and collaborations. 

----------
### Operation: Factor Analysis_Density
##### Overview
The purpose of this effort was to perform Factor Analysis on the data set, finalDenC.csv. A total of 7 "trial runs" were done, each having its own documentation on the results and troubleshooting performed as a result from the trial prior, as well as some commentary regarding what was being reported.

##### Input
finalDenC.csv

##### Output
N/A

##### Packages used
tidyverse psych REdaS tidyr dplyr readxl

----------
### Operation: PCA and FA_Density
##### Overview
Based on the previous attempt (Factor Analysis_Density) at performing factor analysis head-on, the data set proved too much for the CPU to handle, given that around 5 million observations (1306 observations for 4350 variables) produced an estimated 9 million degrees of freedom. Bartlett Tests of Sphericity and Kaiser-Meyer-Olikin tests were performed on the data and yielded inadequate results, largely in part due to the sheer size of the data and the complications it brings. Bartlett tests performed reported a standard deviation of 0, chi-square value of "NA", 9454726 degrees of freedom, and a p-value of 0. Kaiser-Meyer-Olikin tests also yielded results that were on the same note, stating that the overall Measure of Sampling Adequacy (MSA), as well as the individual MSA for each variable accounted for, were "NA". Both processes proved to expensive as well, requiring a majority if not all the RAM available on the machine, taking an hour respectively for each run. Reproduction of results not recommended, as it processes in place were very limited for further work.

Moving forward, the task at hand was to perform Principal Component Analysis on data set, finalDenC.csv, with the Factor Analysis being applied to each respective Principal Component. Doing so was hoped to give way to clustering/ relationships based on physiological function, or rather, cytokine/gene product pathways that the certain genes share with one another.

##### Input
finalDenC.csv

##### Output
N/A

##### Packages used
tidyverse psych REdaS tidyr dplyr readxl stat

----------
### Operation: ReSTRUCTURE
##### Overview
The purpose of this op was to generate correlation matrices for each Structure-ID, with respect to both DENSITY and INTENSITY data sets, and then perform screenings for gene pairs that showcased 70-90% correlation with one another. The algorithm in place for test trials proved to be faulty, as the generated data frames containing the gene pairs only displayed the pairings Snap47-3 had with other genes, including itself. Op was later scrapped and revised (refer to documentation regarding Operation: ReDEMPTION).

##### Input
finalDenC, finalIntC

##### Output
N/A

##### Packages used
readxl dplyr corrplot doMC

----------
### Operation: ReDEMPTION (DEN_Corr, INT_Corr)
##### Overview
A reboot of Operation: ReSTRUCTURE, the purpose of this op was to generate correlation matrices for each respective Structure-ID, with respect to both DENSITY and INTENSITY data sets, and screen each one generated for gene pairings that showcased a correlation value of 90% or higher. High correlation was thought to demonstrate a possible shared gene/physiological pathway between the two genes in question.

##### Input
NewDenC.csv, NewIntC.csv

##### Output
11 .csv files containing gene pairs that showcase a 90% correlation or higher with one another. Structure-ID 253 was left out from analysis due to the fact that it only has one voxel attributed to it, making a correlation matrix and analysis not plausible.

##### Packages used
tidyverse tidyr dplyr readxl corrplot doMC caret

----------
### Operations: DEN_GenePrint and INT_GenePrint
##### Overview
The purpose of this op was to look into the correlation matrices produced in Operations DEN_Corr and INT_Corr, and screen through each respective Structure-ID's correlation matrix for gene pairings that showcase a 90% correlation or higher. The algorithm in place proved to be faulty and inefficient/inaccurate, as it was supposed to remove self/elective pairings (gene paired to itself), as well as duplicate pairings from the generated lists. Op was later scrapped and revised (Please refer to documentation regarding Operation: JVC).

##### Input
NewDenC.csv, NewIntC.csv

##### Output
11 .csv files that contained lists of gene pairs that were thought to not contain any elective pairings or duplicates.

##### Packages used
tidyverse tidyr dplyr readxl corrplot doMC caret

----------
### Operation: JVC
##### Overview
A reboot of Operations: DEN/INT_GenePrint, the purpose of this op was to also look into the correlation matrices produced in Operations DEN_Corr and INT_Corr, and screen through each respective Structure-ID's correlation matrix for gene pairings that showcase a 90% correlation or higher. Tasks and output were delegated to various functions/modules, in the hope that data can be generated that could lead to further measurement analyses, like community searches and gene networking. Collaboration between myself and Jorge Pineda and Vincent Dizon, CoBAaB's Summer 2023 high school interns. Initial coding/algorithm was done using R, in the form of the DEN and INT _CorrScraper modules. Remaining op's code was written in Go, courtesy of Vincent.

##### Jorge's GitHub links:

<https://blitzzard.github.io/>

<https://github.com/Blitzzard/Blitzzard.github.io>

##### Vincent's GitHub links:

<https://vfdizon.github.io/>

<https://github.com/vfdizon/StructureIDs>

##### Input
NewDenC.csv, NewIntC.csv

##### Workflow/Output
"*" = filler symbol, DEN/INT  //  [module/function]

1. NewDenC.csv/ NewIntC.csv -> [*_CorrScraper] -> *_CorrPairs_dirty
2. *_CorrPairs_dirty -> [Vincent_Bypass] -> *_CorrPairs_cleaned
3. *_CorrPairs_cleaned -> [Tita_geneE] -> *_shared (and master_shared)
4. *_shared -> [Tita_chismE] -> *_unique
5. *_unique -> [fingerprints] -> *_fingerprints
6. *_CorrPairs_cleaned -> [Tita_pinkE] -> *_unique_pinke

----------
### Operation: DEN/INT_reCorr
A continuation of the previously-run correlational analyses, the purpose of this op was to tighten the initial 90% correlation threshold imposed on the data, in an effort to look at highly-correlated pairs and alternative means to performing dimension reduction on the dataset.

Logistical/summary statistics were pulled from the data, which included:
1. Voxel distribution across Structure-IDs
2. Number of 90% correlated gene pairs per Structure-ID, in a given DEN/INT data frame
3. Number of active genes per Structure-ID, in a given DEN/INT data frame
4. Number of inactive genes per Structure-ID, in a given DEN/INT data frame

It was made apparent that there was a significant amount of gene pairs still leftover, and so it was then decided to gradually increase the threshold in progressive increments, following a crescendo pattern. Starting at 90%, the correlation threshold was then increase to 99%, 99.9%, 99.99%, and so on and so forth. The results were then graphed accordingly, where the number of correlated gene pairs were totaled and displayed over each benchmark.

Despite wishful thinking that the newly generated data could prove to be much easier to incorporate/implement to prior data visualization/gene networking tools, some interesting findings were found. For both, DEN and INT data frames, as the correlation threshold increased, it became more evident that near-perfect, or even "perfect", correlations were being showcased between a given set of gene pairs. Further analysis revealed that these "perfectly-correlated" gene pairs were given correlation values of "1" not because of similar/same gene expression values across all voxels, but rather the same overall gene expression pattern in terms of being active or not in a given voxel.

This specific finding within the correlation results helped us gain insight into how a given correlation between two genes in calculated. Based on the built-in Pearson correlation formula, cor(i,j) = cov(i,j)/[stdev(i)*stdev(j)], if the values of ith or jth variable have no variation, the resulting standard deviation will be zero, giving an "NaN" value as a result.

In terms of the generated lists of genes that are uniquely inactive i each Structure-ID, those are valid and unchanged, because they are inactive thorugh all voxels (within a given structure) and showcase no variation. This further explained why is was easy to pinpoint and remove such genes altogether from the generated correlation matrices, as well as why some genes are still inlcuded in calculations despite being inactive for a majority of voxels.

This ultimately led us to take a look at the raw data once more, and consider other possible angles at performing dimension reduction and/or dealing with noise. Please refer to documentation regarding Operation: [Current Work]

##### Input
nu_brain_DenC.csv, nu_brain_NewIntC.csv

#### Output
Gene_logistics.xlsx

----------
### Operation: [Current Work]
A continuation of the previous op, Operation: DEN/INT_reCorr, the purpose of this op was to build on the insight gained from the in-depth correlational analysis based on the Coronal DEN and INT data frames and look into possible avenues to implement dimension reduction and mitigate noise.

The brainScan() function was created to act as a diagnostic tool, to look closer at the distribution of the gene expressions for a given data frame, by perform categorical binning analysis.

Bins were set accordingly:

1. 0 to 0.000001
2. 0.000001 to 0.00001
3. 0.00001 to 0.0001
4. 0.0001 to 0.001
5. 0.001 to 0.002
6. 0.001 to 0.01
7. 0.01 to 0.1
8. 0.1 and greater
9. -1 (fully inactive)

This not only provided insight into individual data frame-specific distributions, but allowed side-by-side comparisons for Coronal and Sagittal data. Based on the gathered results, this led to the implementation of 0.001, 0.01, and 0.1 threshold cut-offs, where values found below them would be replaced with null/undefined placeholders. This was done in an effort to mitigate/remove noise and insignificant gene activity.

This led to the creation of the neuralyzer() function. For any given data frame (DEN_Coronal, INT_Coronal, DEN_Sagittal, INT_Sagittal), the function loads and reads through it, implementing the three previously-mentioned thresholds, and identifying resulting voxels (rows) and genes (columns) that showcase NaN values throughout the entire data frame, as well as a total respective count of each.The DEN_Coronal data frame was used as a starting point.

The three newly-generated dataframes are as listed...

1. wakeup_NewDenC_[0.001]_noNaN.csv
2. wakeup_NewDenC_[0.01]_noNaN.csv
3. wakeup_NewDenC_[0.1]_noNaN.csv

What remained evident, however, was that despite voxels (rows) and genes (columns) being removed, the data frame in question contained brief "gaps" of inactivity.

This led to the creation of the suture() function, which took one of the three previously-mentioned data frames as input, and removed rows and columns with NaN values based on given or automatically determined screening thresholds in the form percentages. This additional screening yielded revised, more concise data frames. More specifically, 644- and 193-gene "complete" data frames were generated that showcase full activity across all voxels, based on the [0.001] and [0.01] Coronal DEN data frames, respectively.

The current tasks at the moment are developing separate functions that perform k-means clustering and HAC, and project the results into a 3D space.

