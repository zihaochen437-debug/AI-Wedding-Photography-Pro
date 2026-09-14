# Phase B｜工作模式、产品、套系、Look 与 Scene

> v2.0.0 开发规则。仅当人物标准阶段 `9/9 APPROVED + FROZEN` 后进入。

## 1. PHASE_B_WORK_MODE_GATE

进入任何 Suite / Style / Look / Scene 规划之前，必须先让用户选择：

A. **Ai自动｜AI_AUTO**：Skill 主动分析需求并提出方案，在用户已经授予的范围内自动完成创意规划与执行；不自动取得故事或分镜自主权。

B. **自动｜PRESET_AUTO**：优先调用经过验证的商业预设和默认规划器，用户在关键阶段审核。

C. **半自动｜SEMI_AUTO**：推荐商业默认。用户决定主要方向，Skill 补齐妆造、Scene、道具、Shot 和技术细节并逐阶段确认。

D. **自定义｜CUSTOM**：用户提出更细的风格、服装、妆容、发型、道具、场景、摄影、影视要求，Skill 负责专业化整理、冲突检查与执行编译。

硬规则：

- `WORK_MODE_DOES_NOT_BYPASS_QC`；
- 工作模式不自动等于 `STORY_AUTONOMY` 或 `STORYBOARD_AUTONOMY`；
- 用户可以中途提高人工控制程度，已批准资产继续有效，不得无故重做。

## 2. PROJECT_OUTPUT_TYPE_GATE

工作模式确认后再确定：

A. 只制作婚纱照片  
B. 只制作婚纱影视  
C. 照片 + 婚纱影视

有照片进入 `TARGET_PHOTO_COUNT_GATE`；有视频进入对应视频产品与审批流程。

## 3. TARGET_PHOTO_COUNT_GATE

先问最终独立保留照片数量：6 / 9 / 12 / 18 / 24 / 36 / 48+ / 自定义 / AI 推荐。不是候选数或生成次数。

软规划：

- 6–9：1 个主要视觉方向
- 12–18：约 1–2 个方向 / Look / Scene
- 24–36：2–3 个主要方向，多 Scene / Sequence
- 48+：完整多套系、多 Look、多 Scene

不是死公式；用户明确需要极简、单场景、固定机位或其他创意时允许有理由偏离。

## 4. BROAD_CHOICE_PRESENTATION_POLICY

### FULL_CATALOG_MODE
用户说“全部、都有什么、多看看、没想好”时按大类展示完整商业范围。

### RECOMMENDATION_MODE
已有偏好时推荐 6–10 个真正有视觉跨度的方向，同时提供：更多同类 / 完整分类 / 自定义 / 上传参考。

能力范围包括但不限于：经典、韩式清透、法式轻奢、现代极简、高定影棚、高级时装/Editorial、电影纪实、电影情绪、复古胶片、草坪、森林、海边/礁石、山野/草原、花海/湖边、城市街拍/夜景、欧式建筑、法式室内、新中式、秀禾/龙凤褂、汉服/明制/宋制、民国、东方高定、旅行、艺术情绪、创意实验。

预设是商业起点，不是能力边界；用户上传的服装、妆容、发型、场景、姿势、灯光、构图、故事和自定义创意优先。

## 5. 多选与独立分支

Suite / Style / Look / Scene / 产品比例可以多选，但默认建立独立 `SUITE-0N` 分支，不把多个方向塞进一个 Prompt。用户明确选择“融合”时才建立受控复合风格。

## 6. SUITE → STYLE → LOOK → SCENE

婚纱摄影与婚纱线默认：

`SUITE → STYLE → BRIDE LOOK PLAN → AB04 → GROOM LOOK PLAN → AB05 → LOOK REVIEW → PROP → SCENE PLAN → AB06 → DIRECTOR / BLOCKING / CAMERA / STORYBOARD`

AB04/AB05 分别审核冻结后才可把 Look 阶段视为完成；AB06 建立前确认当前 Look 与 Scene 的时代、色彩、材质和使用场景兼容。

## 7. LOOK_NAME_IS_NOT_GENERATION_PROMPT

“法式清透”“韩式”“新中式”“高定”“电影纪实”等只是 UI / 方案名称，必须经过 `LOOK_PROFILE_RESOLVER` 展开。

### 新娘 Look Resolver

`identity_anchor / makeup / hair / dress / fabric / silhouette / neckline / sleeves / waist / skirt_train / veil / headpiece / earrings / necklace / shoes / visible_jewelry / personal_signatures / forbidden_changes`

### 新郎 Look Resolver

`identity_anchor / grooming / hair / suit_or_costume / shoulder_line / lapel_or_collar / shirt / tie_or_bow / waistcoat_or_cummerbund / cufflinks / trousers / shoes / boutonniere / watch_ring / fabric / personal_signatures / forbidden_changes`

## 8. BRIDE_MAKEUP_REQUIRED / EXPLICIT_MAKEUP_COMPILATION

AB04 第一版正式生成必须明确存在可执行的新娘妆面描述，除非用户明确选择“无妆/极近原貌妆”。不得只写“精致新娘妆”“法式妆容”。

妆面至少解析：

`base_and_complexion / skin_finish / brows / eyeshadow / eyeliner / lashes / under_eye / blush / contour / highlight / lips / intensity / texture_retention`

执行原则：

- 化妆不得擅自改变真实脸型、眼距、鼻形、嘴形、下颌或年龄身份；
- 保留真实皮肤纹理，不用厚磨皮制造“妆”；
- Frozen Retouch Profile 是人物皮肤/精修基线，Makeup Resolver 在其上增加化妆状态，不再次美容；
- 传统/年代/文化妆面与服装、发型、饰品和 Scene 保持一致。

## 9. LOOK_PROMPT_PREFLIGHT

生成 AB04/AB05 前检查：

- 是否真实绑定 M01 及必要 U/F/D 身份资产；
- 是否解析用户选择的 Look，而不是只发送名称；
- 新娘妆容是否包含可见眉眼、唇、肤质和强度信息；
- 发型、头纱、饰品与礼服是否冲突；
- 是否保留用户个人标志；
- 是否存在未经授权的年轻化、瘦脸、体型改变或五官重设计；
- Prompt 是否只保留当前任务必要信息。

未通过：`LOOK_GENERATION_BLOCKED`。

## 10. MAKEUP_PRESENCE_GATE / LOOK_IDENTITY_GATE

AB04 审核分别判断：

1. Identity Fidelity；
2. Makeup Presence & Accuracy；
3. Hair / Wardrobe / Accessory；
4. Editability。

“脸像但几乎没化妆”和“妆容漂亮但不像本人”都不能通过。

## 11. LOOK_EDIT_FIRST / MAKEUP_REVISION_SCOPE_LOCK

Look 某一域不合格时优先在当前正确版本上局部编辑，不默认重生整张。

例如只调整眼妆：只开放眼影、眼线、睫毛和必要连接区域；冻结脸型、其他五官、新郎、发型、婚纱、饰品、Scene、Camera 与已正确肤质。

修改后再次执行 `LOOK_IDENTITY_GATE`，防止 `MAKEUP_IDENTITY_DRIFT`。

## 12. 商业能力目录

### 新娘
妆面、发型、婚纱轮廓、领口、袖型、腰线、裙摆/拖尾、面料、蕾丝/刺绣/珠饰、头纱、头饰、耳饰、项链、鞋履等，且包括但不限于这些预设。

### 新郎
面部整理、发型、西装/礼服版型、肩线、翻领/立领、衬衫、领带/领结、马甲/腰封、袖扣、裤型、鞋履、胸花、手表/戒指、面料与配色，且允许剧情或用户自定义服装体系。

### 道具
花束、团扇、伞、茶具、香槟杯、书、乐器、车辆、宠物、家具、纪念物等；记录谁拿、哪只手、握持点、高度、方向和另一只手状态。清单包括但不限于这些示例。

### 传统与历史风格
服装、妆发、饰品、道具和 Scene 需要时代/文化一致性；用户自有服装和自定义参考优先。