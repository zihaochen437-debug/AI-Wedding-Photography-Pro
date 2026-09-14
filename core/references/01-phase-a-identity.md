# Phase A｜人物身份、参考资料与精修

> v2.0.0 开发规则。Phase A 必须严格单项串行：一次只处理一个当前核心问题或资产，用户未明确确认不得进入下一项。

## 1. 参考准备与上传方式

先说明：参考资料质量决定人物高保真的上限，但资料不足不剥夺用户继续创作的选择。

进入 `REFERENCE_UPLOAD_MODE_GATE`：

A. 新娘、新郎、双人混合上传  
B. 单人分批上传  
C. 先新郎，再新娘  
D. 先新娘，再新郎  
E. 自定义顺序

混合上传后整理：`BRIDE_REFERENCES / GROOM_REFERENCES / COUPLE_REFERENCES / UNRESOLVED_REFERENCES`。归属不清必须询问，不得猜。

## 2. 两级补充确认

人物级：每完成一人资料接收后询问是否还补正面、45°、侧面、背面、全身、手部、个人特征等。

项目级：正式资产制作前再次询问是否补新娘、新郎、双人并排全身、身高/体型/年龄、个人特征、身体结构/辅助器具或其他。只有用户明确“没有，按当前资料继续”才关闭 intake。

## 3. 真人参考最低与推荐标准

最低高保真：新娘、新郎各至少 1 张清晰正面标准人像。资料只有正面也允许继续，但必须提示 45°、侧面、背面和身体结构将更多依赖 AI 推断。

商业推荐每人：正面半身、鼻尖朝画面左侧约45°、鼻尖朝画面右侧约45°、左完整侧面、右完整侧面、背面半身；双人再提供同一地面、同一前后平面的并排直立全身照。

无真人参考则进入 `AI_CREATIVE`，不得宣称真人高保真还原。

## 4. S/A/B/C/D 评级与职责

每张参考图同时记录质量等级与职责：正面身份、左45、右45、左侧面、右侧面、全身、双人比例、个人特征、辅助、排除。

不同参考照片不能平权平均；正式生成只使用 `MINIMUM_SUFFICIENT_REFERENCE_PACK`。

原图足够标准时优先裁切、背景统一、曝光、白平衡、清晰度和必要自然处理；不要为了“统一”重新造一个 AI 人物。缺失角度才允许 AI 推演，且推演结果不得反写成用户真实证据。

## 5. 身体可见性与个人标志

不可见区域区分：`REFERENCE_CROPPED / REFERENCE_OCCLUDED / ANGLE_NOT_VISIBLE / BODY_STRUCTURE_UNCERTAIN`。

个人特征由用户指定：长期保留、仅标准资产保留、随套系调整、移除、自定义。可包括眼镜、美瞳、耳饰、项链、戒指、手表、痣、雀斑、疤痕、纹身、胡须、牙齿、发际线、假肢、轮椅、拐杖及其他用户主动提供的信息。

AI 创作性身体补全必须独立分支、单独审批，不反写为真实人物标准。

## 6. RETOUCH_BEFORE_STANDARD_ASSET

R0–R4 必须在第一张正式人物资产生成前确定。UI 档位名称不是生产 Prompt，执行时必须经过 `RETOUCH_PROFILE_RESOLVER` 展开成具体可见要求。

- **R0 原貌级**：只做标准化所需的曝光、白平衡、背景、清晰度与明显技术瑕疵处理；不主动年轻化、瘦脸、磨平皮肤、改变体型或消除个人标志。
- **R1 自然级**：轻度整理暂时性皮肤问题、油光、飞发和牙面色差；保留毛孔、真实纹理、年龄感、脸型与个人标志。
- **R2 商业自然级**：默认推荐。均匀但不塑料化的肤色与皮肤整理，适度减轻暂时性黑眼圈/泛红/油光，整理眉毛、发丝、胡须、牙齿与肩颈姿态；保持真实骨相、五官比例、年龄、体量与可识别特征。
- **R3 商业强化级**：在 R2 基础上允许更明显的商业级皮肤、轮廓光影、发丝、牙齿、手部和体态整理；除非用户明确授权，仍不得改变脸型、眼鼻唇结构、真实身高或体型类别。
- **R4 用户定制级**：逐项按用户明确要求执行，并继续受身份不变量、真实结构和安全边界约束。

### RETOUCH_PROFILE_RESOLVER

每个档位解析为以下域：

`skin / face_geometry / eyes / brows / nose / lips_teeth / hair_beard / neck_shoulders / hands / body_posture / body_contour / personal_signatures / forbidden_changes`

编译链：

`USER UI → RETOUCH PROFILE ID → PROFILE RESOLVER → USER OVERRIDES → PERSONAL SIGNATURE POLICY → IDENTITY INVARIANT → TASK FILTER → NATURAL LANGUAGE COMPILER`

硬规则：

- `RETOUCH_UI_LABEL_IS_NOT_PROMPT`：不得只把“R2 商业自然级”等标签发送给图片模型。
- `STANDARD_ASSET_ALREADY_RETOUCHED`：第一张正式标准资产输出时就已经是用户批准的精修状态，不再建立“未精修标准照”和“精修标准照”两套人物母版。
- 后续 U/F/D、双人标准照和 AB04/AB05 必须继承同一精修基线；禁止再次加入“更年轻、更漂亮、更瘦、提升颜值”等无授权二次美容导致 `RETOUCH_DRIFT`。
- 精修状态不等于妆容状态。婚礼妆面在 Phase B 的 Look Resolver 中独立处理。

## 7. STANDARD_WARDROBE_SELECTION_GATE

人物标准资产使用简洁、自然、无明显 Logo/复杂花纹的标准服装，并在首张正式标准资产前确认一套男女协调方案，之后贯穿双方 4 张单人标准资产与双人正面全身标准照。

候选仅为商业预设，不是能力边界：

- CW-01 黑白经典
- CW-02 奶油白 / 深海军蓝
- CW-03 暖白 / 深棕
- CW-04 浅蓝 / 深蓝
- CW-05 黑 / 象牙白
- CW-06 用户自定义 / 保留原服装

不得默认把男女标准服装统一改成灰色。

## 8. STANDARD_IDENTITY_4_PLUS_1_POLICY

每位人物只有 4 个正式人物标准输出槽位：

1. `FRONT_MEDIUM_MASTER`｜正面中景标准照
2. `UPPER_BODY_STANDARD_BOARD`｜上半身标准资产板
3. `FULL_BODY_STANDARD_BOARD`｜全身标准资产板
4. `DETAIL_STANDARD_BOARD`｜人物特写细节资产板

双人仅增加 1 张：

5. `COUPLE_FRONT_FULL_BODY_MASTER`｜双人正面全身标准照

双人项目人物标准阶段唯一有效的物理输出数量为：`4 + 4 + 1 = 9 images`。

多视角只存在于 U/F/D 资产板内部，不再把左45、右45、左右侧面、背面等分别注册成新的正式人物资产。板内区域失败时冻结正确区域，只修失败区域并升级同一槽位版本；不得新增第 5 张单人人物标准资产。

## 9. Phase A 顺序

`启动介绍 → 参考指南 → 上传模式 → 上传/分类 → 人物级补充 → 项目级最终补充 → S/A/B/C/D + 职责 → 人物资料 → 个人特征/身体策略 → R0–R4 + Retouch Resolver → 标准服装 → 新娘 M/U/F/D 逐项审核冻结 → 新郎 M/U/F/D 逐项审核冻结 → 双人正面全身标准照审核冻结 → 9/9 APPROVED + FROZEN → PHASE A COMPLETE`

Phase A 未达到 `9/9 APPROVED + FROZEN` 时，不得把人物标准阶段标记为完成。