**Title:** Swara TTS: A Prosody-Aware Sanskrit Chanting Text-to-Speech System

**Abstract:**
This paper introduces **Swara TTS**, a novel **Sanskrit Śloka Chanting text-to-speech (TTS) system** designed to address the challenge of making vast Sanskrit literary works—such as the Mahābhārata (comprising over 100,000 ślokas), Purāṇas, and Kāvya-s—accessible through synthetic chanting. Unlike traditional TTS models that focus on spoken language, Swara TTS integrates phonetic precision, pitch modulation (Swara), rhythmic cadence (Chandas or meter), and expressive prosody to generate metrically aligned, natural chanting. We experiment with three advanced generative speech models—F5, VoiceCraft, and Parler-TTS—trained on a curated dataset sourced from Avinash Varna & Hrishikesh Terdalkar's audio alignment efforts and IITK’s Gita Supersite, comprising 64 hours of annotated ślokas from the Rāmāyaṇa and Bhagavad Gītā. These models are evaluated through objective and subjective metrics to identify the most suitable candidate for high-quality chanting synthesis.

**1. Introduction:**
While speech synthesis technologies have advanced significantly, generating natural and prosody-aligned chanting remains a formidable challenge—particularly for Sanskrit ślokas, which demand precise melody, rhythm, and metrical adherence. The Mahābhārata, with over 100,000 ślokas, stands as the largest literary work in the history of mankind, making comprehensive human-led chanting recording an impractical endeavor. This challenge equally applies to other monumental Sanskrit texts like the Purāṇas and Kāvya-s. In the experimental phase, we initially trained VoiceCraft and VITS models on 6 hours of Bhagavad Gītā, but overfitting prompted a shift to more robust architectures—F5, VoiceCraft, and Parler-TTS—alongside a much richer 58-hour Ramayana dataset. Interestingly, even early overfitted models produced compelling Anuṣṭubh Chanda chanting. The dominance of Anuṣṭubh in the dataset, however, led to a realization: model bias towards this meter, necessitating broader chandas distribution for equitable prosody learning. *Swara TTS* aims to address this by synthesizing metrically accurate and tuneful chanting, preserving literary heritage while serving as a valuable tool for Sanskrit learners, enthusiasts, and Sanātanis. It ensures continuity and accessibility of sacred texts for generations to come.

**2. Background and Motivation:**
Sanskrit poetry is deeply rooted in structured metrical systems (Chandas) and tonal recitation (Swara). Classical works such as Mahābhārata, Purāṇas, and various Kāvya-s require chanting that is aligned not just with pronunciation but with musical and prosodic elements. Existing TTS systems fail to capture these dimensions. Our approach is to evaluate state-of-the-art generative speech models to assess their ability to render śloka chanting naturally and expressively.

**3. System Architecture:**
We experiment with three candidate models:
- **F5**: A fast, lightweight generative TTS model
- **VoiceCraft**: A zero-shot expressive voice synthesis framework
- **Parler-TTS**: A high-quality, transformer-based TTS model

**4. Data Preparation:**
We curated a 64-hour dataset from the Rāmāyaṇa and Bhagavad Gītā, sourced from the audio alignment efforts by Avinash Varna & Hrishikesh Terdalkar and IITK’s Gita Supersite. The data includes time-aligned text, swara markings, and chandas annotations. Chandas distribution analysis revealed a heavy dominance of Anuṣṭubh, highlighting the need for a more balanced dataset for comprehensive chanting synthesis. For chandas labeling, we leveraged **Hrishikesh Terdalkar’s Chandojnanam**, an algorithm designed for Chandas identification of Sanskrit text. Prosodic labels were manually verified and pitch contours extracted using advanced pitch-tracking algorithms.

**5. Training and Evaluation:**
The models were fine-tuned and evaluated using objective metrics such as mel-cepstral distortion (MCD), F0 RMSE, and intelligibility scores. Subjective evaluations were conducted via Mean Opinion Score (MOS) ratings by Sanskrit scholars and trained chanters.

**6. Results:**
Swara TTS demonstrated significant improvements in melodic alignment, chandas consistency, and naturalness of output. Among the three, [best-performing model] achieved the highest MOS and lowest distortion metrics.

**7.  Tools and Applications Developed as Part of This Research:**
- Laya: Audio-Text Alignment & Annotation Tool developed to enable precise synchronization and labeling for chanting synthesis.
- Chandas-Sloka Visualizer: A tool to analyze and visualize chandas structures and their occurrence across the dataset.
- Smruthi: An interactive reading platform designed for end-user engagement with Itihāsas, Purāṇas, and Kāvya-s, powered by Swara TTS outputs.

**8. Potential Usecases:**
- Audio rendering of śloka and classical texts
- AI chanting tutors for education and learning
- Archival voice synthesis of lost texts
- Assistive tools for visually impaired users

**9. Future Work:**
The current dataset’s chandas sparsity necessitates further expansion. We propose building a comprehensive dataset—**SwaraSangraha**—with equitable distribution across major chandas through a combination of manual recordings and automated online discovery. This includes detailed chandas labeling (including guru-laghu mapping), swara labeling (via MIDI or pitch quantization), and robust audio-text alignment tools to support scalable and culturally accurate chanting synthesis.

**10. Conclusion:**
Swara TTS is a pioneering attempt to bring Sanskrit śloka chanting into the AI era. It bridges the gap between linguistic fidelity and musical expressiveness, setting a foundation for scalable and culturally faithful chanting synthesis systems.

**Keywords:** Swara TTS, Chanting TTS, Sanskrit Prosody, Chandas, Swara, Voice Synthesis, F5, VoiceCraft, Parler-TTS, SwaraSangraha, Chandojnanam

