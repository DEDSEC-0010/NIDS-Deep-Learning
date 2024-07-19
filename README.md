# Network Intrusion Detection using Deep Learning and Explainable AI

## Project Overview

In today’s interconnected world, cyber threats pose significant risks to individuals, organizations, and governments, emphasizing the critical need for robust cybersecurity measures. Traditional security approaches struggle to keep pace with the evolving nature of cyber threats. Our project introduces a novel approach that integrates deep learning and explainable AI into intrusion detection systems to enhance network security. By leveraging deep learning’s adaptability, the system aims to detect anomalies and previously unseen attack patterns. The incorporation of explainable AI enhances transparency, fostering human understanding and trust in the security system.

## Table of Contents

1. [Introduction](#introduction)
2. [Background](#background)
3. [Literature Survey](#literature-survey)
4. [Methodology](#methodology)
5. [Dataset](#dataset)
6. [Design Interface and Networks](#design-interface-and-networks)
7. [Implementation Details](#implementation-details)
8. [Results](#results)
9. [Conclusion](#conclusion)
10. [References](#references)

## Introduction

In today’s interconnected world, cyber threats pose significant risks to individuals, organizations, and governments, emphasizing the critical need for robust cybersecurity measures. Traditional security approaches struggle to keep pace with the evolving nature of cyber threats. Our project introduces a novel approach that integrates deep learning and explainable AI into intrusion detection systems to enhance network security.

## Background

Traditional network intrusion detection systems (NIDS) rely on predefined rules and signatures, making them less effective against new and evolving threats. Our project aims to address these limitations by leveraging deep learning and explainable AI techniques.

## Literature Survey

- Network Intrusion Detection System using Deep Learning
- Systematic study of machine learning and deep learning approaches
- Network Intrusion Detection for Cyber Security using Unsupervised Deep Learning Approaches
- Understanding LIME explainability
- Optimized LIME Explanations
- Stabilized-LIME for Model Explanation
- Adversarial Attacks on Post hoc Explanation Methods
- Intrusion detection using CNN and SHAP models
- Interpretation of machine learning models using Shapley values
- Counterfactual Shapley Additive Explanations

## Methodology

![Methodology](path/to/methodology_image.png)

## Dataset

The dataset used is CIC-IDS2018, consisting of over 80 features and 1 million connections data.

![Data Samples](path/to/data_samples_image.png)

## Design Interface and Networks

![Network Architecture](path/to/network_architecture_image.png)

![Pipeline Architecture](path/to/pipeline_architecture_image.png)

![User Interface](path/to/ui_designs_image.png)

## Implementation Details

1. **Dataset Collection**: The Network Intrusion Benchmark Dataset CIC-IDS2018 is collected.
2. **Data Preprocessing**: The dataset is transformed according to our model.
3. **Model Training**: The model is trained with the transformed data using 18,561 trainable parameters.
4. **Database Creation and Data Storage**: A database is created to store the model results as blob values.
5. **Data Pipeline Integration**: A data pipeline is created to simulate real traffic flow through our Intrusion Detection System.
6. **Euclidean Distance Computation**: The Euclidean distance between the upcoming traffic and the stored log values is computed.
7. **Explainability**: The explainability of each feature is determined using SHAP values.

![Final Classification and Logs](path/to/final_classification_image.png)

## Results

![Confusion Matrix](path/to/confusion_matrix_image.png)

![SHAP Values](path/to/shap_values_image.png)

![Data Pipeline](path/to/data_pipeline_image.png)

## Conclusion

This project demonstrates the value of integrating deep learning and explainable AI into intrusion detection systems. These technologies enhance the efficacy of identifying and mitigating cyber threats, strengthening network defenses. The transparency provided by explainable AI fosters human understanding and trust in the security system. As cyber threats evolve, continuous innovation is essential to safeguard our digital infrastructure. Embracing these technologies is crucial for effectively combating modern cyber threats.

## References

1. Ashiku, L., & Dagli, C. (2021). Network intrusion detection system using deep learning. *Procedia Computer Science, 185*, 239–247.
2. Al-Emadi, S., Al-Mohannadi, A., & Al-Senaid, F. (2020). Using deep learning techniques for network intrusion detection. In *2020 IEEE international conference on informatics, IoT, and enabling technologies (ICIoT)*, pp. 171–176. IEEE.
3. Ahmad, Z., Khan, A. S., Wai Shiang, C., Abdullah, J., & Ahmad, F. (2021). Network intrusion detection system: A systematic study of machine learning and deep learning approaches. *Transactions on Emerging Telecommunications Technologies, 32*(1), e4150.
4. Alom, M. Z., & Taha, T. M. (2017). Network intrusion detection for cyber security using unsupervised deep learning approaches. In *2017 IEEE national aerospace and electronics conference (NAECON)*, pp. 63–69. IEEE.
5. Zhang, Y., Song, K., Sun, Y., Tan, S., & Udell, M. (2019). "Why should you trust my explanation?" understanding uncertainty in LIME explanations. arXiv preprint arXiv:1904.12991.
6. Visani, G., Bagli, E., & Chesani, F. (2020). OptiLIME: Optimized LIME explanations for diagnostic computer algorithms. arXiv preprint arXiv:2006.05714.
7. Zhou, Z., Hooker, G., & Wang, F. (2021). S-LIME: Stabilized-LIME for model explanation. In *Proceedings of the 27th ACM SIGKDD conference on knowledge discovery & data mining*, pp. 2429–2438.
8. Slack, D., Hilgard, S., Jia, E., Singh, S., & Lakkaraju, H. (2020). Fooling LIME and SHAP: Adversarial attacks on post hoc explanation methods. In *Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society*, pp. 180–186.
9. Younisse, R., Ahmad, A., & Abu Al-Haija, Q. (2022). Explaining intrusion detection-based convolutional neural networks using Shapley additive explanations (SHAP). *Big Data and Cognitive Computing, 6*(4), 126.
10. Rodríguez-Pérez, R., & Bajorath, J. (2020). Interpretation of machine learning models using Shapley values: Application to compound potency and multi-target activity predictions. *Journal of computer-aided molecular design, 34*, 1013–1026.
11. Albini, E., Long, J., Dervovic, D., & Magazzeni, D. (2022). Counterfactual Shapley additive explanations. In *Proceedings of the 2022 ACM Conference on Fairness, Accountability, and Transparency*, pp. 1054–1070.
12. Dataset: [CIC-IDS2018](https://www.unb.ca/cic/datasets/ids-2018.html)

## Acknowledgements

This project was supervised by Mr. Jayakrishnan A, Department of Artificial Intelligence and Data Science, Jyothi Engineering College, Cheruthuruthy.

## Contributors

- Aswathi Krishna P T (JEC20AD017)
- Athvik S (JEC20AD018)
- Josten S Cheeran (JEC20AD027)
- Sreehari Sreejay O P (JEC20AD047)
