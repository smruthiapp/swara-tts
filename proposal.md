# Swara TTS Research and Development Proposal

## **Swara TTS: Prosody-Aware Sanskrit Chanting Model for Large-Scale Sloka Generation**

**Proposed by:** Radhe Shyam Salopanthula (AI4Bharat)

**Contributors:**  
- Radhe Shyam Salopanthula (AI4Bharat)
- Shubodeep Chanda (M.Tech, IIT Madras)  
- Tanmay Garde (M.Tech, IIT Madras)
  
**Advisors:**  
- Prof. Mitesh M. Khapra (Head of AI4Bharat; Professor, IIT Madras)  
- Praveen S. V. (Lead TTS Researcher, AI4Bharat; PhD Scholar, IIT Madras)

## 1. Problem Statement
Swara TTS aims to develop a prosody-aware **text-to-speech (TTS)** system capable of accurately generating **Sanskrit sloka recitations** with correct intonation, rhythm, and metrical structure (Chandas). Proper prosody is critical for Sanskrit verses – almost all Sanskrit poetry follows strict meter (chandas) ([Prosody | Learn Sanskrit Online](https://www.learnsanskrit.org/supp/prosody/#:~:text=Almost%20all%20Sanskrit%20poetry%20is,must%20start%20with%20the%20Vedas)), and in recitation the intonation is guided by melody and rhythm rather than plain text structure ([Bertsokantari: a TTS Based Singing Synthesis System](https://www.isca-archive.org/interspeech_2016/blanco16_interspeech.pdf#:~:text=prosodic%20point%20of%20view%2C%20in,exhibits%20higher%20intensity%20with%20a)). However, building such a specialized TTS is challenging because **Sanskrit TTS research is very limited** (only one notable prior attempt by Mishra et al. is cited) ([](https://arxiv.org/pdf/2212.03558#:~:text=is%20a%20need%20for%20producing,10)). This project has a dual objective: 

1. **Research Goal:** Explore and evaluate multiple advanced TTS architectures (F5-TTS, VoiceCraft, and Indic Parler TTS) to determine the best approach for **structured, prosody-rich speech synthesis** in Sanskrit slokas.  
2. **Practical Goal:** Use the chosen model to automatically generate an **audio corpus of ~1.5 lakh Mahabharata slokas**, effectively creating the *first-ever complete* audio rendition of the Mahabharata. Given the epic’s enormity (around 100,000 shlokas, ~1.8 million words ([18 Parvas of Mahabharata - TemplePurohit - Your Spiritual Destination | Bhakti, Shraddha Aur Ashirwad](https://www.templepurohit.com/18-parvas-mahabharata/#:~:text=Mahabharata%20is%20one%20of%20the,The%20eighteen%20parvas%20are))), a full manual recording is impractical – an AI-driven solution is the only feasible way to achieve this scale.

Beyond model training, the synthesized corpus will power **“Smruthi”**, an interactive platform for public access to Sanskrit literature (Puranas, Itihasas, and other ancient texts) with features like translations, word-by-word meanings, and linguistic annotations. In summary, Swara TTS tackles a significant research problem in speech synthesis and addresses a cultural need by making Sanskrit epics **audibly accessible** to all.

## 2. Existing Resources and Data
To train the TTS models, we will leverage a rich collection of **text-audio aligned datasets** in Sanskrit:

- **Datasets compiled by IIT Kanpur:** A curated set of classical Sanskrit works with their audio, including *Amarakosha*, *Ashtadhyayi*, *Meghaduta*, *Ramayana* (58 hours of audio, covering ~18,000–19,000 slokas), *Tarkasamgraha*, and *Patanjali Yogasutras*. These provide a large base of spoken Sanskrit verses for training.  
- **Additional Data Sources:** We will incorporate ~20 hours of multi-speaker recitations from the *Bhagavad Gita*, which adds diversity in voice and style. We will also use the **Indic Parler TTS** dataset/models (already optimized for accurate Sanskrit pronunciation) ([ai4bharat/indic-parler-tts · Hugging Face](https://huggingface.co/ai4bharat/indic-parler-tts#:~:text=match%20at%20L407%20Sanskrit%2099,and%20natural%20voices%20for%20underrepresented)). In addition, a proprietary tool named **“Laya”** will aid in precise sloka segmentation and text-audio alignment, ensuring high-quality pairing of verses with their recitation audio.

All datasets include aligned Sanskrit text and corresponding audio. We will begin with potentially imperfect alignments and progressively refine them. High-accuracy alignment (using Laya) is especially important for capturing the correct timing of syllables and pauses according to Sanskrit **chandas** (metrical patterns).

## 3. Research Exploration: Model Training and Evaluation
We will **train and evaluate three different TTS models** to identify the most effective architecture for prosody-aware Sanskrit speech synthesis. Each model will be handled by a team member in parallel:

- **F5-TTS:** A cutting-edge non-autoregressive TTS system based on flow-matching diffusion transformers ([[2410.06885] F5-TTS: A Fairytaler that Fakes Fluent and Faithful Speech with Flow Matching](https://arxiv.org/abs/2410.06885#:~:text=%3E%20Abstract%3AThis%20paper%20introduces%20F5,We%20further%20propose)). F5-TTS has demonstrated highly natural and expressive speech output, with efficient training and inference (real-time factor ~0.15) ([[2410.06885] F5-TTS: A Fairytaler that Fakes Fluent and Faithful Speech with Flow Matching](https://arxiv.org/abs/2410.06885#:~:text=easily%20applied%20to%20existing%20flow,checkpoints%20to%20promote%20community%20development)). It was trained on a massive 100,000 hour multilingual dataset and exhibits strong zero-shot voice capabilities and even code-switching fluency ([[2410.06885] F5-TTS: A Fairytaler that Fakes Fluent and Faithful Speech with Flow Matching](https://arxiv.org/abs/2410.06885#:~:text=greatly%20improved%20compared%20to%20state,checkpoints%20to%20promote%20community%20development)). We will evaluate how well this state-of-the-art model can be adapted to Sanskrit sloka chanting. *(Lead: Shubodeep Chanda)*

- **VoiceCraft:** A recently introduced Transformer-based neural codec TTS model known for **zero-shot** voice cloning and editing ([VoiceCraft](https://jasonppy.github.io/VoiceCraft_web/#:~:text=VoiceCraft%20is%20a%20token%20infilling,audiobooks%2C%20internet%20videos%2C%20and%20podcasts)). VoiceCraft achieves state-of-the-art performance on in-the-wild data and can clone an unseen speaker’s voice with only a few seconds of audio ([VoiceCraft](https://jasonppy.github.io/VoiceCraft_web/#:~:text=VoiceCraft%20is%20a%20token%20infilling,audiobooks%2C%20internet%20videos%2C%20and%20podcasts)). This makes it promising for generating chants in a consistent voice even with limited speaker data. We will test VoiceCraft’s ability to maintain the required rhythm and intonation of Sanskrit verses out-of-the-box and with fine-tuning. *(Lead: Tanmay Garde)*

- **Indic Parler TTS:** An existing multilingual TTS model from AI4Bharat/HuggingFace that supports 20+ Indian languages including Sanskrit ([ai4bharat/indic-parler-tts · Hugging Face](https://huggingface.co/ai4bharat/indic-parler-tts#:~:text=Indic%20Parler,Sindhi%2C%20Tamil%2C%20Telugu%2C%20and%20Urdu)). It’s designed for high-quality pronunciation and even offers an expressive style prompt. Notably, Indic Parler TTS achieves **near-perfect synthesis quality for Sanskrit**, making it ideal for classical use cases ([ai4bharat/indic-parler-tts · Hugging Face](https://huggingface.co/ai4bharat/indic-parler-tts#:~:text=match%20at%20L407%20Sanskrit%2099,and%20natural%20voices%20for%20underrepresented)). We will extend this model specifically for chanting by injecting prosody features (metrical and pitch information). This serves as a strong baseline given its native Sanskrit support. *(Lead: Radhe Shyam Salopanthula)*

**Training Strategy:** All three models will initially be trained on the full corpus of available data (including some imperfect alignments) to gauge their baseline performance. We will then fine-tune each model on a smaller, **precisely segmented** subset of data (ensuring each sloka’s audio is perfectly aligned and annotated with meter) to see how much the prosody and clarity improve. Throughout, we will evaluate each model on key criteria: **speech clarity**, correctness of **rhythm/timing**, and adherence to the intended **intonation pattern** of the chants.

Comparative evaluation will reveal which architecture best captures the nuanced prosody of Sanskrit slokas. The outcomes of Phase 1 will guide us in selecting a single model (or a fusion of techniques) for the large-scale generation in Phase 2.

## 4. Feature Engineering and Model Enhancements
To successfully synthesize authentic Sanskrit chanting, we will incorporate several custom features and conditioning mechanisms into the TTS models:

- **Text-Audio Alignment:** Using the *Laya* interface and other alignment tools, we ensure that each syllable of the text maps to the correct timing in audio. Precise alignment is crucial for maintaining the **metrical rhythm** – any misalignment can distort the meter and the understood content. We will enforce alignment during training so the model learns the correct duration for long vs. short syllables as defined by the meter.

- **Chandas Labeling (Meter Tags):** Each Sanskrit verse (sloka) will be tagged with its metrical pattern (e.g., Anushtubh, Shardulavikridita, etc.). By feeding the **meter information** as an additional input, the model can be conditioned to maintain the right number of syllables and rhythmical emphasis per line. This helps preserve the structure of the verse in speech (the pattern of stresses and pauses that come from the metrical template) ([Prosody | Learn Sanskrit Online](https://www.learnsanskrit.org/supp/prosody/#:~:text=Almost%20all%20Sanskrit%20poetry%20is,must%20start%20with%20the%20Vedas)).

- **Swara (Pitch) Encoding with MIDI:** We will encode intended intonation patterns as a sequence of musical notes (MIDI pitch values) aligned with the text. Essentially, this provides a melody contour for the chant. Incorporating these **pitch and rhythm annotations** guides the model’s prosody output, much like how singing synthesis uses a given melody for intonation ([Bertsokantari: a TTS Based Singing Synthesis System](https://www.isca-archive.org/interspeech_2016/blanco16_interspeech.pdf#:~:text=prosodic%20point%20of%20view%2C%20in,exhibits%20higher%20intensity%20with%20a)). For example, a rising pitch at the end of a quarter-verse or a specific cadence at a line break can be learned by the model. This MIDI-based swara labeling will capture the traditional chanting tune which is not evident from text alone.

- **Expressive and Natural Speech Synthesis:** While the primary focus is on chanted recitation, we will also extend the chosen model to produce **spoken Sanskrit** (non-chant, natural prosody). This involves training the model with more varied intonation patterns (e.g., question vs. statement, emotional tone) possibly using the Indic Parler TTS capabilities. The goal is to ensure the model isn’t limited to a monotonic chant, but can also read Sanskrit texts in a natural narrative style when needed (useful for translations or commentary). Techniques like style tokens or prompt-based voice descriptions ([[2402.01912] Natural language guidance of high-fidelity text-to-speech with synthetic annotations](https://arxiv.org/abs/2402.01912#:~:text=%3E%20Abstract%3AText,method%20to%20a%2045k%20hour)) ([[2402.01912] Natural language guidance of high-fidelity text-to-speech with synthetic annotations](https://arxiv.org/abs/2402.01912#:~:text=dataset%2C%20which%20we%20use%20to,heard%20at%20this%20https%20URL)) may be employed to control expressiveness.

These feature engineering steps will be implemented during model training and fine-tuning. By encoding **what to speak (text)** along with **how to speak it (meter, pitch, style)**, we enable the TTS system to generate highly authentic and engaging Sanskrit audio output.

## 5. Research Contribution and Expected Outcomes

**Phase 1 (First 6 Months):** In the initial research phase, we will focus on model development and comparative analysis. Key activities include:  
- Training all three candidate TTS models (F5-TTS, VoiceCraft, Indic Parler TTS) on the available Sanskrit datasets, and iterating on alignment and preprocessing to improve input quality.  
- Evaluating each model’s output for **clarity of speech**, **accuracy of rhythm** (does the recitation follow the correct meter beat?), and **prosody adherence** (intonation matching the expected chant pattern). We will use both objective metrics and subjective evaluation by Sanskrit experts.  
- Expanding the system’s vocabulary and pronunciation coverage. Sanskrit has complex sandhi (euphonic combination) rules and a large vocabulary; we will ensure uncommon words and names from the epics are synthesized correctly, possibly by augmenting training with those examples.  
- Documenting the findings: which model performs best in which aspect, challenges observed (e.g., a model might be good at clarity but poor at rhythm, etc.), and strategies to overcome them. This will form the basis of an **M.Tech project report** for the student contributors detailing the Phase 1 experiments.

**Phase 2 (Next 6 Months):** In the second phase, we will scale up and deploy the solution using the insights from Phase 1. Activities include:  
- **Optimizing the best-performing model** for long-form narration. This involves improving efficiency (so it can generate hours of audio continuously) and stability (to avoid error accumulation in very long sequences). We may need to implement breathing/pause logic so the audio sounds natural over lengthy recitations.  
- Generating the complete **Mahabharata audio corpus (~150,000 slokas)**. This will be done iteratively, possibly book by book (parva by parva), verifying quality at intervals. The result will be the first exhaustive audio version of the Mahabharata in Sanskrit ([18 Parvas of Mahabharata - TemplePurohit - Your Spiritual Destination | Bhakti, Shraddha Aur Ashirwad](https://www.templepurohit.com/18-parvas-mahabharata/#:~:text=Mahabharata%20is%20one%20of%20the,The%20eighteen%20parvas%20are)), created entirely through AI voice synthesis.  
- Integrating the AI-generated audio into the **Smruthi** platform. This includes developing a user-friendly interface where listeners can navigate the epic by chapter/verse, read the text with translations while listening to the recitation, and experience interactive features (like clicking a word to hear its meaning). We will host the corpus for public access, effectively making this vast literary work accessible to anyone as an audiobook-like experience.  
- Compiling the full research findings, model details, and results into an **MS Thesis** (for the lead researcher) and writing a **research paper (“Swara TTS”)** for publication. The paper will describe our prosody-aware TTS methodology, the challenges of Sanskrit TTS, and the results of the project, thereby contributing to the academic community.

**Academic Contributions:** By the end of the project, we expect several academic outputs: (a) M.Tech project reports summarizing Phase 1 results for the student contributors; (b) an MS thesis covering the entire research; and (c) a standalone peer-reviewed research paper on Sanskrit prosody-aware TTS. We also plan to release the **AI-generated audio corpus** and possibly the fine-tuned model weights as an open dataset/resource, which would be invaluable for linguists, digital humanities researchers, and further TTS research in low-resource languages.

## 6. Timeline & Milestones (12-Month Plan)

| Phase                 | Duration      | Key Activities                                             |
|-----------------------|--------------:|------------------------------------------------------------|
| **Phase 1**           | 6 months      | Model training & evaluation; data alignment & expansion; interim report documenting findings. |
| **Phase 2**           | 6 months      | Model optimization for scale; generate full Mahabharata corpus; Smruthi platform integration. |
| **Final Deliverables**| End of Month 12 | MS Thesis submission; Research paper draft; Public release of synthesized corpus and model. |

*(Regular checkpoints:* monthly progress reviews with advisors, and a mid-year evaluation to decide the model for Phase 2.)*

## 7. Conclusion
Swara TTS is an ambitious project at the intersection of **language technology and cultural preservation**. On the research front, it will push the boundaries of TTS by incorporating fine-grained prosody control for a classical language, demonstrating how modern speech synthesis can handle not just casual speech but also **structured, melodic recitations**. The development of a prosody-aware Sanskrit TTS can serve as a blueprint for other languages and domains where intonation is critical (for example, scripture chanting, poetry, or singing synthesis). 

On the application front, the project delivers tangible output with immense cultural value: the **first AI-generated complete audio of the Mahabharata**. The Mahabharata, with over 100,000 verses, is one of the longest poetic works in the world ([18 Parvas of Mahabharata - TemplePurohit - Your Spiritual Destination | Bhakti, Shraddha Aur Ashirwad](https://www.templepurohit.com/18-parvas-mahabharata/#:~:text=Mahabharata%20is%20one%20of%20the,The%20eighteen%20parvas%20are)), and creating a full audio rendition has remained beyond reach until now. By leveraging AI, we are able to preserve and disseminate this epic in auditory form, something that can greatly aid in its study and appreciation. Integrating this into *Smruthi* (along with other texts like the Ramayana, Puranas, etc.) will make Sanskrit literature far more accessible. Students and enthusiasts will be able to listen to authentic renditions of verses while reading translations and notes, bridging the gap between traditional scholarship and modern technology.

In conclusion, Swara TTS is poised to make significant **academic contributions** in speech synthesis and have a **real-world impact** by preserving Sanskrit oral traditions digitally. It exemplifies how AI can amplify human efforts – here, by generating in a year what would otherwise take lifetimes of recitation. The success of this project could open doors to similar initiatives for other heritage texts and languages, ensuring that ancient wisdom echoes in the modern world.

**Next Steps:**  
- Begin the Phase 1 training process with all three candidate models in parallel, using the compiled datasets.  
- Implement the proposed *Swara* (pitch) and *Chandas* (meter) conditioning mechanisms in the model training pipeline, and validate on a few sample slokas.  
- Rigorously evaluate early outputs with domain experts to fine-tune the approach, and finalize the choice of TTS architecture for Phase 2 large-scale generation. 

